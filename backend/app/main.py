from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlmodel import SQLModel

from fastapi.middleware.cors import CORSMiddleware

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

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST", "PATCH", "DELETE"],
    allow_headers=["Content-Type"],
)

app.include_router(tasks_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}