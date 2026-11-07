from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlmodel import SQLModel

from app.api.routes.tasks import router as tasks_router
from app.db.base import Task
from app.db.session import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Attempting database connection...")

    try:
        SQLModel.metadata.create_all(engine)
        print("Database connection successful.")
    except Exception as error:
        print("DATABASE CONNECTION FAILED:")
        print(error)
        raise

    yield


app = FastAPI(
    title="Household Tasks API",
    lifespan=lifespan,
)

app.include_router(tasks_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}