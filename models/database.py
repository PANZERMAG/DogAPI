from fastapi.security import APIKeyHeader
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from models import models

DATABASE_URL = "sqlite:///pet_api.sqlite"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

FindPetsBD = declarative_base()

api_key_header = APIKeyHeader(name="X-API-Key")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
