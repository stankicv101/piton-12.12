from pydantic import BaseModel
from datetime import date 

class StudentSchema(BaseModel):
    name: str 
    age: int 
    grade: str 
    enrollment_date: date 

class StudentCreate(StudentSchema):
    pass 

class StudentUpdate(StudentSchema):
    pass 
