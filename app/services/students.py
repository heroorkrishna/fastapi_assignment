# app/services/students.py

from app.models.students import Students  
from app.schemas.students import StudentCreate
from sqlalchemy import func
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session, joinedload
from app.services.main import AppService, AppCRUD
from sqlalchemy.orm import Query


class StudentService(AppService):
    
    def create_student(self, student: StudentCreate):
        
        max_id = self.db.query(func.max(Students.id)).scalar() or 0
        i = 1
        
        db_student = Students(
            id=max_id + i,
            name=student.name,
            total_marks=student.total_marks
        )
        self.db.add(db_student)
        self.db.commit()
        
        return {
            "status_code": status.HTTP_201_CREATED,
            "message": "Student created successfully",
            "student": {
                "id": db_student.id,
                "name": db_student.name,
                "total_marks": db_student.total_marks
            }
        }
        

        
class StudentCrud(AppCRUD):
    
    def get_students_pagination(self, page: int = 1, page_size: int = 2):
        query: Query = self.db.query(Students)

        total_items = query.count()
        total_pages = (total_items + page_size - 1) // page_size

        if page < 1 or page > total_pages:
            raise HTTPException(status_code=404, detail="Page out of bounds")

        offset = (page - 1) * page_size
        students = query.limit(page_size).offset(offset).all()

        if not students:
            raise HTTPException(status_code=404, detail="Students not found")

        return {
            "total_pages": total_pages,
            "current_page": page,
            "students": [
                {
                    "id": student.id,
                    "name": student.name,
                    "total_marks": student.total_marks
                }
                for student in students
            ]
        }
        
    def filter_students(self, name: str, total_marks: float):
        
        get_data = self.db.query(Students).all()
        
        filtered_data = []
        
        filtered_data.append({
            "name":get_data[0].name,
            "total_marks":get_data[0].total_marks
        })
        
        if name:
            filtered_data = [student for student in get_data if student.name == name]
        
        if total_marks:
            filtered_data = [student for student in get_data if student.total_marks == total_marks]
            
        return {
                "status_code": status.HTTP_200_OK,
                "data": filtered_data
                }
        