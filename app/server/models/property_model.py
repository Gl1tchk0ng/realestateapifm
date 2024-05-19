from typing import Optional, Any
from pydantic import BaseModel, Field

class PropertySchema(BaseModel):
    property_id: int = Field(...)
    property_name: str = Field(...)
    address: str = Field(...)
    city: str = Field(...)
    state: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "property_id": 1,
                "property_name": "Green Villa",
                "address": "123 Main Street",
                "city": "Jaipur",
                "state": "Rajasthan",
            }
        }

class UpdateProperty(BaseModel):
    property_name: Optional[str]
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "property_name": "Blue Villa",
                "address": "456 Elm Street",
                "city": "Delhi",
                "state": "Delhi",
            }
        }

def ResponseModel(data: Any, message: str):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error: Any, code: int, message: str):
    return {"error": error, "code": code, "message": message}
