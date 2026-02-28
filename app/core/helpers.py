from fastapi import Request , HTTPException , status , Depends
from app.core.config import settings
from sqlalchemy.orm import Session
import jwt
from jwt.exceptions import InvalidTokenError
from app.models.user_models import UserModel
from app.db import get_db


def is_authenticated(request : Request , db : Session = Depends(get_db)):
    try:
        token = request.headers.get("authorization")
        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="You are UNAUTHORIZED")

        token = token.split(" ")[-1]
        data = jwt.decode(token , settings.SECRET_KEY , algorithms=[settings.ALGORITHM])
        user_id = data.get("sub")

        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token payload"
            )

        # Username Validation
        user = db.query(UserModel).filter(UserModel.id == user_id).first()

        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="You are UNAUTHORIZED")
        

        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired"
        )

    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )