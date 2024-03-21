from typing import Optional
from pydantic import BaseModel

class StudentBase(BaseModel):
    id: Optional[int] = None
    name: str
    total_marks: float

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    slno: int

    class Config:
        orm_mode = True