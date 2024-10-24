from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from broker.rabbitmq import rabbit_connection
from db.db import get_session

runner_router = APIRouter()

@runner_router.post('/', status_code=status.HTTP_201_CREATED)
async def create_model(
    id: int,
    db: AsyncSession = Depends(get_session)
) -> dict:
    """
    Создание запроса на вычисление модели по ID.
    """
    rabbit_connection._send_message(model_id=id)
    response = {
        'model_id': id,
        'status': 'send'
    }
    return response
