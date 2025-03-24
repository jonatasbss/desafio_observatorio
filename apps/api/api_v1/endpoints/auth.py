from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from apps.core.database import get_db
from apps.core.security import create_access_token, blacklist_token, is_token_blacklisted
from apps.crud import crud_user
from apps.schemas.token import TokenWithUserDetails

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login", auto_error=False)


class LoginRequest(BaseModel):
    email: str
    password: str


def get_token(token: str = Depends(oauth2_scheme)):
    if not token:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Token is required"
        )
    return token

@router.post("/login", response_model=TokenWithUserDetails)
def login(form_data: LoginRequest, db: Session = Depends(get_db)):
    user = crud_user.authenticate(db, email=form_data.email, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(subject=user.id)
    return {"access_token": access_token, "token_type": "bearer", "id": user.id, "name": user.name, "email": user.email,
            "document": user.document}


@router.post("/logout", status_code=status.HTTP_200_OK)
def logout(token: str = Depends(get_token), db: Session = Depends(get_db)):
    if is_token_blacklisted(db, token):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Token already blacklisted")

    blacklist_token(db, token)

    return {"message": "Successfully logged out"}
