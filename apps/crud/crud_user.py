from typing import Optional, List, Type
from apps.models.user import User
from fastapi import HTTPException
from sqlalchemy.orm import Session
from apps.schemas.user import UserCreate, UserUpdate
from apps.core.security import verify_password, get_password_hash


def get_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()


def get_all_users(db: Session) -> list[Type[User]]:
    return db.query(User).all()


def get_user(db: Session, user_id: int) -> Optional[User]:
    user = db.query(User).filter(User.id == user_id).first()
    return user


def create_user(db: Session, *, obj_in: UserCreate) -> User:
    existing_user = get_by_email(db, obj_in.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    db_obj = User(
        email=obj_in.email,
        hashed_password=get_password_hash(obj_in.password),
        name=obj_in.name,
        phone=obj_in.phone,
        document=obj_in.document,
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update_user(db: Session, user_id: int, obj_in: UserUpdate) -> User:
    db_obj = get_user(db, user_id=user_id)
    if db_obj:
        for field, value in obj_in.dict(exclude_unset=True).items():
            setattr(db_obj, field, value)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    raise HTTPException(status_code=404, detail="User not found")

def delete_user(db: Session, user_id: int) -> User:
    db_obj = get_user(db, user_id=user_id)
    if db_obj:
        db.delete(db_obj)
        db.commit()



def authenticate(db: Session, *, email: str, password: str) -> Optional[User]:
    user = get_by_email(db, email=email)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user
