from fastapi import APIRouter

from .models_router import router
from .runner import runner_router

api_router = APIRouter()
api_router.include_router(router, prefix='/models', tags=['models'])
api_router.include_router(runner_router, prefix='/runner', tags=['runner'])