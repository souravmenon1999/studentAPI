import uuid
from bson import ObjectId
from fastapi import APIRouter, HTTPException, Path

def generate_custom_id():
    return str(uuid.uuid4())


def validate_object_id(id: str) -> ObjectId:
    try:
        return ObjectId(id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ObjectId")