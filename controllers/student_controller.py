from fastapi import APIRouter, HTTPException, Path
from models.student_model import Student
from schemas.student_schema import StudentCreate, StudentUpdate
from services.mongo_service import students_collection
from utils.id_utils import generate_custom_id, validate_object_id
from typing import List, Optional
from bson import ObjectId


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
        
        async for student in students_collection.find(query,{"name": 1, "age": 1, "_id": 0}):
            
            students.append(student)
        
        return {"data": students}
    
    except Exception as e:
       
        raise HTTPException(status_code=500, detail=f"Error fetching students: {str(e)}")



@router.get("/students/{id}", response_model=Student)
async def fetch_student(id: str = Path(..., description="The ID of the student previously created.")):
    obj_id = validate_object_id(id)
    student = await students_collection.find_one({"_id": obj_id})
    if not student:
        raise HTTPException(status_code=404, detail="Student not found.")
    student["id"] = str(student.pop("_id"))  
    return student

@router.patch("/students/{id}", status_code=204)
async def update_student(
    id: str = Path(..., description="The ID of the student to update."),
    student_update: StudentUpdate = None
):
    obj_id = validate_object_id(id)
    update_data = {k: v for k, v in student_update.dict(exclude_unset=True).items()}

    if not update_data:
        raise HTTPException(status_code=400, detail="No data provided for update.")

    result = await students_collection.update_one({"_id": obj_id}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Student not found.")
    return None

@router.delete("/students/{id}", status_code=200)
async def delete_student(id: str = Path(..., description="The ID of the student to delete.")):
    obj_id = validate_object_id(id)
    result = await students_collection.delete_one({"_id": obj_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found.")
    return {"detail": "Student deleted successfully."}