from fastapi import APIRouter, HTTPException
from models.student_model import Student
from schemas.student_schema import StudentCreate
from services.mongo_service import students_collection
from utils.id_utils import generate_custom_id
from typing import List, Optional

router = APIRouter()

@router.post("/students", status_code=201)
async def create_student(student: StudentCreate):
   
    student_data = student.dict()

    try:
       
        result = await students_collection.insert_one(student_data)

        # Return the MongoDB-generated _id as the 'id'
        return {"id": str(result.inserted_id)}  
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error creating student: " + str(e))


@router.get("/students", response_model=dict)
async def list_students(age: Optional[int] = None, country: Optional[str] = None):
    query = {}
    
    # age filter
    if age is not None:
        query["age"] = {"$gte": age}
    
    # country filter
    if country is not None:
        query["address.country"] = country
    
    try:
        students = []
        # Fetch data
        async for student in students_collection.find(query):
            student["id"] = str(student.pop("_id"))  
            students.append(student)
        
        return {"data": students}
    
    except Exception as e:
       
        raise HTTPException(status_code=500, detail=f"Error fetching students: {str(e)}")