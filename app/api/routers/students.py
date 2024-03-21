# app/routers/students.py

from typing import Optional
from fastapi import APIRouter, Depends
from fastapi.responses import  JSONResponse
from app.db.database import  get_db
from app.schemas.students import StudentCreate
from app.services.students import StudentCrud, StudentService

router = APIRouter()

@router.post("/create-students")
def create_students(Student: StudentCreate, db: get_db = Depends()):
    
    result = StudentService(db).create_student(Student)
    return JSONResponse(status_code=200, content=result)
    
    
@router.get("/get-students")
def get_students(db: get_db = Depends()):
    
    result = StudentCrud(db).get_students_pagination()
    return JSONResponse(status_code=200, content=result)

@router.get("/filter-students")
def filter_students(name: Optional[str]=None, total_marks: Optional[float]=None ,db: get_db = Depends()):
    
    result = StudentCrud(db).filter_students(name=name, total_marks=total_marks)
    return result