import logging
from app.schemas.user_schemas import UserSchema, LoginSchema
from sqlalchemy.orm import Session
from app.models.user_models import UserModel
from fastapi import HTTPException, status 
from pwdlib import PasswordHash
import jwt
from datetime import datetime, timedelta, timezone
from app.core.config import settings

logger = logging.getLogger(__name__)


password_hash = PasswordHash.recommended()

def get_password_hash(password) -> str:
    return password_hash.hash(password)

def verify_password(plain_password , hashed_password) -> bool:
    return password_hash.verify(plain_password , hashed_password)

def register_service(body : UserSchema , db : Session):

    # Username Validation
    logger.info("Register attempt for username=%s" , body.username)
    is_user = db.query(UserModel).filter(UserModel.username == body.username).first()

    if is_user:
        logger.warning("Duplicate username | username=%s", body.username)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exist..")
    
    # Email Validation
    is_user = db.query(UserModel).filter(UserModel.email == body.email).first()

    if is_user:
        logger.warning("Duplicate email | email=%s", body.email)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email-Address already exist..")

    # Password Hashing
    hash_password = get_password_hash(body.password)

    # Creating a Object of a User-model

    new_user = UserModel(
        name = body.name,
        username = body.username,
        hash_password = hash_password,
        email = body.email
    )

    # Store in DataBase
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    logger.info("User registered | username=%s", new_user.username)
    return new_user 


def login_service(body: LoginSchema, db: Session):

    logger.info("Login attempt for username=%s" , body.username)

    user = (
        db.query(UserModel)
        .filter(UserModel.username == body.username)
        .first()
    )

    if not user or not verify_password(body.password, user.hash_password):
        logger.warning("Login failed | username=%s", body.username)
        raise HTTPException(  
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

 
    exp_time = datetime.now(timezone.utc) + timedelta(
        seconds=settings.EXP_TIME_IN_SEC
    )

    token = jwt.encode(
        {
            "sub": str(user.id), 
            "exp": exp_time
        },
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    logger.info("Login success | username=%s", body.username)
        

    return {
        "access_token": token,
        "token_type": "bearer"
    }

    

