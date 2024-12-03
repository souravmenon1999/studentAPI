from pydantic import BaseModel, Field

class Address(BaseModel):
    city: str = Field(..., description="City is required")
    country: str = Field(..., description="Country is required")

class StudentCreate(BaseModel):
    name: str = Field(..., description="Name is required")
    age: int = Field(..., ge=0, description="Age is required and must be a positive integer")
    address: Address

from pydantic import BaseModel

class StudentUpdate(BaseModel):
    name: str | None = None
    age: int | None = None
    address: Address | None = None


    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "age": 20,
                "address": {
                    "city": "New York",
                    "country": "USA"
                }
            }
        }
