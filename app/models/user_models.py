from sqlalchemy import Column , String , Integer 
from app.db import Base
from sqlalchemy.orm import relationship

class UserModel(Base):

    __tablename__ = "user_table"

    id = Column(Integer , primary_key=True , index=True)
    name = Column(String)
    username = Column(String , nullable=False)
    hash_password = Column(String , nullable=False)
    email = Column(String)

    tasks = relationship(
        "TaskModel",
        back_populates="user",
        cascade="all, delete-orphan"
    )