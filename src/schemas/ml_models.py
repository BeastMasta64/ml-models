from datetime import datetime

from pydantic import BaseModel


class CreateModel(BaseModel):
    """Схема для создания и обновления модели."""
    name: str
    description: str
    ml_model_type: str
    ml_model_version: str
    author: str


class GetModel(CreateModel):
    """Схема получения информации о модели."""
    id: int
    created_date: datetime
