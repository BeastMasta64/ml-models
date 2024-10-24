
from typing import Any, Dict, List, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy import delete, select, update

from db.db import AsyncSession
from models.base import Base
from models.ml_models import Model

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class Model_CRUD():

    async def get(
        self,
        id: Any,
        db: AsyncSession,
    ) -> ModelType:
        """Метод для получения объекта модели по ID."""
        statement = select(Model).where(Model.id == id)
        results = await db.execute(statement=statement)
        return results.scalar_one_or_none()

    async def get_list(
        self,
        db: AsyncSession,
    ) -> List[ModelType]:
        """Метод для получения списка моделей."""
        statement = select(Model)
        results = await db.execute(statement=statement)
        return results.scalars().all()

    async def create(
        self,
        obj_in: CreateSchemaType,
        db: AsyncSession
    ) -> ModelType:
        """Метод для создания объекта модели."""
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = Model(**obj_in_data)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def update(
        self,
        id: int,
        obj_in: Union[UpdateSchemaType, Dict[str, Any]],
        db: AsyncSession,
    ) -> ModelType:
        """Метод для обновления объекта модели по ID."""
        await db.execute(update(Model).where(
            Model.id == id).values(**jsonable_encoder(obj_in)))
        await db.commit()

        results = await db.execute(select(Model).where(Model.id == id))
        return results.scalar_one_or_none()

    async def delete(
        self,
        id: int,
        db: AsyncSession,
    ) -> ModelType:
        """Метод для удаления объекта модели по ID."""
        await db.execute(delete(Model).where(Model.id == id))
        await db.commit()


model_crud = Model_CRUD()
