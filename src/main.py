import uvicorn
from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from fastapi.responses import ORJSONResponse

from api.base import api_router
from broker.rabbitmq import rabbit_connection
from core.config import app_settings


@asynccontextmanager
async def lifespan(_: FastAPI):
    rabbit_connection.connect()
    yield
    rabbit_connection.disconnect()

app = FastAPI(
    title=app_settings.app_title,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
    lifespan=lifespan
)
app.include_router(api_router, prefix="/api/v1")

if __name__ == '__main__':

    uvicorn.run(
        'main:app',
        host=app_settings.host,
        port=app_settings.port,
    )
