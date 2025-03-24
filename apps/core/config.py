import os
from typing import List
from decouple import config
from pydantic import ConfigDict
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = config("PROJECT_NAME", cast=str)
    PROJECT_VERSION: str = config("PROJECT_VERSION", cast=str)
    API_V1_STR: str = config("API_V1_STR", cast=str)
    ALGORITHM: str = config("ALGORITHM", cast=str)
    SECRET_KEY: str = config("SECRET_KEY", cast=str)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24

    DATABASE_URL: str = config("DATABASE_URL")

    BACKEND_CORS_ORIGINS: str = config("BACKEND_CORS_ORIGINS", "*", cast=str)

    REDIS_URL: str = config("REDIS_URL", default=None)

    def get_cors_origins(self) -> List[str]:
        if self.BACKEND_CORS_ORIGINS == "*":
            return ["*"]
        return [origin.strip() for origin in self.BACKEND_CORS_ORIGINS.split(",")]

    model_config = SettingsConfigDict(case_sensitive=True, extra="allow")


settings = Settings()
