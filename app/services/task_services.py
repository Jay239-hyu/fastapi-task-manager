from app.schemas.task_schemas import Taskschema
from sqlalchemy.orm import Session
from app.models.task_models import TaskModel
from fastapi import HTTPException, status
from app.models.user_models import UserModel

def create_task_service(
    task_data: Taskschema,
    db: Session,
    user: UserModel
    ):

    new_task = TaskModel(
        title=task_data.title,
        description=task_data.description,
        user_id=user.id  # ownership lock
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_all_tasks_service(
    db: Session, 
    user : UserModel
    ):

    tasks = (
    db.query(TaskModel)
    .filter(TaskModel.user_id == user.id)
    .all()
    )
    return tasks

def get_one_task_service(
    task_id: int,
    db: Session,
    user: UserModel
    ):

    task = (
        db.query(TaskModel)
        .filter(
            TaskModel.id == task_id,
            TaskModel.user_id == user.id
        )
        .first()
    )

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return task

def update_task_service(
    task_id: int,
    task_data: Taskschema,
    db: Session,
    user: UserModel
    ):

    task = (
        db.query(TaskModel)
        .filter(
            TaskModel.id == task_id,
            TaskModel.user_id == user.id
        )
        .first()
    )

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    update_data = task_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)

    return task

def delete_task_service(
    task_id: int,
    db: Session,
    user: UserModel
    ):

    task = (
        db.query(TaskModel)
        .filter(
            TaskModel.id == task_id,
            TaskModel.user_id == user.id
        )
        .first()
    )

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    db.delete(task)
    db.commit()

    return 
  

