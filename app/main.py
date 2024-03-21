"""
Main FastAPI application entry point.
"""
import calendar
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings as config
from app.db.database import create_tables

from app.api.routers import students


def get_application():
    """
    Create and initialize a FastAPI application instance.

    Returns:
        FastAPI: The initialized FastAPI application instance.
    """
    app = FastAPI(title=config.PROJECT_NAME, version=config.VERSION)

    create_tables()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
  
    app.include_router(students.router)
    
    #zoom
    return app


app = get_application()
