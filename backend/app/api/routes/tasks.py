from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.db.base import Task, TaskCreate, TaskRead
from app.db.session import get_session

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("", response_model=TaskRead)
def create_task(
    task_data: TaskCreate,
    session: Session = Depends(get_session),
):
    task = Task.model_validate(task_data)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


@router.get("", response_model=list[TaskRead])
def list_tasks(session: Session = Depends(get_session)):
    tasks = session.exec(select(Task)).all()
    return tasks


@router.patch("/{task_id}/complete", response_model=TaskRead)
def complete_task(
    task_id: int,
    session: Session = Depends(get_session),
):
    task = session.get(Task, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.completed = True
    session.add(task)
    session.commit()
    session.refresh(task)
    return task