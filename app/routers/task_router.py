from fastapi import APIRouter, Depends, status
from app.services.task_services import (
    create_task_service,
    get_all_tasks_service,
    get_one_task_service,
    update_task_service,
    delete_task_service,
)
from app.schemas.task_schemas import Taskschema, TaskResponseSchema
from app.db import get_db
from typing import List
from sqlalchemy.orm import Session
from app.core.helpers import is_authenticated
from app.models.user_models import UserModel   

task_router = APIRouter(prefix="/tasks", tags=["Tasks"])

@task_router.post("" , response_model=TaskResponseSchema , status_code = status.HTTP_201_CREATED)
def create_task_endpoint(
    task_data: Taskschema, 
    db: Session = Depends(get_db), 
    user: UserModel  = Depends(is_authenticated)
    ):
    return create_task_service(task_data , db , user)



@task_router.get("" ,response_model=List[TaskResponseSchema] ,  status_code=status.HTTP_200_OK)
def get_all_tasks_endpoint(
    db: Session= Depends(get_db), 
    user: UserModel  = Depends(is_authenticated)
    ):
    return get_all_tasks_service(db , user)



@task_router.get("/{task_id}", response_model=TaskResponseSchema  , status_code=status.HTTP_200_OK)
def get_one_task_endpoint(
    task_id: int, 
    db: Session = Depends(get_db), 
    user: UserModel  = Depends(is_authenticated)
    ):
    return get_one_task_service(task_id , db , user)



@task_router.put("/{task_id}" , response_model=TaskResponseSchema, status_code=status.HTTP_200_OK)
def update_task_endpoint(
    task_id: int, 
    task_data: Taskschema, 
    db: Session = Depends(get_db), 
    user: UserModel  = Depends(is_authenticated)
    ):
    return update_task_service(task_id, task_data, db, user)
 


@task_router.delete("/{task_id}" , status_code=status.HTTP_204_NO_CONTENT)
def delete_task_endpoint(
    task_id: int, 
    db: Session = Depends(get_db), 
    user: UserModel  = Depends(is_authenticated)
    ):
    return delete_task_service(task_id , db , user)
 
