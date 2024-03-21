"""
Configuration for the project.
"""
import base64
import os
from starlette.config import Config
from starlette.datastructures import Secret

class Settings:
    """
    Settings for the database connection
    """
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    config = Config(fileDir + "/.env")

    DATABASE_URL = config("DATABASE_URL")

    PROJECT_NAME = "Assignment"
    VERSION = "1.0.0"
    API_PREFIX = "/api"

    POSTGRES_USER : str = config("POSTGRES_USER", cast=str)
    POSTGRES_PASSWORD : str = config("POSTGRES_PASSWORD", cast=Secret)
    POSTGRES_SERVER : str = config("POSTGRES_SERVER", cast=str, default="db")
    POSTGRES_PORT : str = config("POSTGRES_PORT", cast=str, default="5432")
    POSTGRES_DB : str = config("POSTGRES_DB", cast=str)
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

settings = Settings()
