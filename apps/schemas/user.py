from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    name: str
    phone: str
    document: str


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    name: Optional[str] = None
    phone: Optional[str] = None
    document: Optional[str] = None


class UserInDBase(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class User(UserInDBase):
    pass
