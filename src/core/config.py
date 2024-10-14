import os

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    app_title: str = 'ML_models_API'
    database_dsn: PostgresDsn

    host: str = '127.0.0.1'
    port: int = 8080


app_settings = AppSettings()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
