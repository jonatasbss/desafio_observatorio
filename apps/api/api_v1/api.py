from fastapi import APIRouter
from apps.api.api_v1.endpoints import auth, user, sidra

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(sidra.router, prefix="/sidra", tags=["sidra"])
