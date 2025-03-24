from sqlalchemy import Column, String, DateTime
from apps.core.database import Base
from datetime import datetime


class TokenBlacklist(Base):
    __tablename__ = 'token_blacklist'

    token = Column(String(255), nullable=False, primary_key=True)
    created = Column(DateTime, nullable=False, default=datetime.utcnow)