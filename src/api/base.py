from fastapi import APIRouter

from .ml_models import router

api_router = APIRouter()
api_router.include_router(router, prefix='/models', tags=['models'])
