from typing import Optional

from pydantic import BaseModel, EmailStr,Field


class Student(BaseModel):
    name: str
    age: Optional[int] = None
    email: EmailStr 
    cgpa:float = Field(default=None, ge=0.0, le=4.0, description="CGPA must be between 0.0 and 4.0")

new_student = {"name": "Dipanshu", "age": 20, "email": "abc@gmail.com"}


student = Student(**new_student)
print(student)