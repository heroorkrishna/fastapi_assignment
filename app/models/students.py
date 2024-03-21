from sqlalchemy import Column, Integer, String, Float
from app.db.database import Base
from pydantic import BaseModel 

class Students(Base):
    __tablename__ = "students"
    
    slno = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    id = Column(Integer, nullable=False,unique=True)
    name = Column(String, nullable=False)
    total_marks = Column(Float, nullable=False)