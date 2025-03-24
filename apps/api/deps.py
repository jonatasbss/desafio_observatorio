from typing import Generator, Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from pydantic import ValidationError
from sqlalchemy.orm import Session
from apps.core.config import settings
from apps.core.database import get_db
from apps.models.user import User
from apps.schemas.token import TokenPayload