from sqlalchemy import Column , Integer , String , ForeignKey, Boolean
from app.db import Base
from sqlalchemy.orm import relationship


class TaskModel(Base):
    __tablename__ = "user_tasks"

    id = Column(Integer , primary_key=True , index=True)
    title = Column(String)
    description = Column(String)
    is_completed = Column(Boolean , default=False)


    user_id = Column(Integer, ForeignKey("user_table.id"), nullable=False)  
    user = relationship("UserModel", back_populates="tasks") # ORM Side Relation