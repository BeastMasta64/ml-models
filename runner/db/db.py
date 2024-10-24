import datetime
import os

from sqlalchemy import DateTime, Numeric, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column
from sqlalchemy.sql import func

database_url = os.environ.get("DATABASE_URL")
engine = create_engine(database_url, echo=True)

class Base(DeclarativeBase):
    pass

class Result(Base):
    __tablename__ = 'results'
    delivery_tag: Mapped[int] = mapped_column(primary_key=True)
    #result: Mapped[float]
    result: Mapped[Numeric] = mapped_column(Numeric(10, 5))
    created_date: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

def add_result(delivery_tag, computation_result):
    with Session(engine) as session:
        result = Result(
            delivery_tag=delivery_tag,
            result=computation_result
        )
        session.add(result)
        session.commit()
        session.refresh(result)
