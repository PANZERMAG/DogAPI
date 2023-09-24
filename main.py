from fastapi import FastAPI

from routers.routes import router as rt
from models import models
from models.database import engine

models.FindPetsBD.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(
    router=rt,
    prefix='/api'
)

