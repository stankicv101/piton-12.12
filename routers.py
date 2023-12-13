from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import models, schemas 

router = APIRouter()

@router.get("/students/", response_model=List[schemas.StudentSchema])
def read_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()

@router.get("/students/{student_id}", response_model=schemas.StudentSchema)
def read_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if student is None:
        raise HTTPEXCeption(status_code=404, detail="Student not found")
    return student