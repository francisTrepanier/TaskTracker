from datetime import datetime, timezone
from sqlmodel import SQLModel, Field


class TaskBase(SQLModel):
    title: str
    notes: str | None = None
    completed: bool = False


class Task(TaskBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class TaskCreate(TaskBase):
    pass


class TaskRead(TaskBase):
    id: int
    created_at: datetime