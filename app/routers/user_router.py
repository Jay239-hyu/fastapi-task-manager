from fastapi import APIRouter, Depends, status 
from sqlalchemy.orm import Session
from app.schemas.user_schemas import (
UserSchema, 
UserResponseSchema, 
LoginSchema,
TokenResponseSchema
)
from app.db import get_db
from app.services.user_services import register_service, login_service


user_router = APIRouter(prefix="/auth" , tags=["Auth"])

@user_router.post("/register" , response_model= UserResponseSchema, status_code=status.HTTP_201_CREATED)
def register_endpoint(
    body: UserSchema, 
    db: Session = Depends(get_db)
    ):
    return register_service(body , db)

@user_router.post("/login", response_model=TokenResponseSchema, status_code=status.HTTP_200_OK)
def login_endpoint(
    body: LoginSchema, 
    db: Session = Depends(get_db)
    ):
    return login_service(body , db)

