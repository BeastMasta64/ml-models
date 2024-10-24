from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from db.db import get_session
from schemas.ml_models import CreateModel, GetModel
from services.ml_models import model_crud

router = APIRouter()


@router.get('/', response_model=List[GetModel], status_code=status.HTTP_200_OK)
async def read_models(
    db: AsyncSession = Depends(get_session),
) -> Any:
    """
    Получение всех моделей из бд.
    """
    model = await model_crud.get_list(db=db)
    return model


@router.get('/{id}', response_model=GetModel, status_code=status.HTTP_200_OK)
async def read_model(
    *,
    db: AsyncSession = Depends(get_session),
    id: int,
) -> Any:
    """
    Получение модели по ID.
    """
    model = await model_crud.get(db=db, id=id)
    if not model:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Модель не найдена'
        )
    return model


@router.post('/', response_model=GetModel, status_code=status.HTTP_201_CREATED)
async def create_model(
    model_in: CreateModel,
    db: AsyncSession = Depends(get_session)
) -> Any:
    """
    Создание новой модели.
    """
    model = await model_crud.create(db=db, obj_in=model_in)
    return model


@router.put('/{id}', response_model=GetModel, status_code=status.HTTP_200_OK)
async def update_model(
    id: int,
    model_in: CreateModel,
    db: AsyncSession = Depends(get_session),
) -> Any:
    """
    Обновление модели по ID.
    """
    model = await model_crud.update(db=db, id=id, obj_in=model_in)
    if not model:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Модель не найдена'
        )
    return model


@router.delete('/{id}',
               response_model=None,
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_model(
    id: int,
    db: AsyncSession = Depends(get_session),
) -> Any:
    """
    Удаление модели по ID.
    """
    await model_crud.delete(db=db, id=id)
