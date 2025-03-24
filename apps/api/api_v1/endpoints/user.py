from typing import List
from apps.core.security import get_current_user
from apps.crud import crud_user
from sqlalchemy.orm import Session
from apps.core.database import get_db
from apps.schemas.user import UserCreate, User, UserUpdate
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()


@router.get("/users", response_model=List[User])
def list_users(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    users = crud_user.get_all_users(db)
    return users


@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user = crud_user.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/users", response_model=User)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    user = crud_user.create_user(db=db, obj_in=user_in)
    return user


@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user_in: UserUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user = create_user.get_by_id(db=db, id=user_in.id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    updated_user = crud_user.update_user(db=db, user_id=user_id, obj_in=user_in)
    return updated_user


@router.patch("/users/{user_id}", response_model=User)
def patch_user(user_id: int, user_in: UserUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user = crud_user.get_user(db=db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    updated_user = crud_user.update_user(db=db, user_id=user_id, obj_in=user_in)
    return updated_user


@router.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user = crud_user.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    crud_user.delete_user(db=db, user_id=user_id)
    return {"message": "User deleted successfully"}
