from fastapi import APIRouter, HTTPException
from typing import List
from server.crud import PropertyCRUD
from server.database import parse_property_result
from server.models.property_model import PropertySchema, UpdateProperty

router = APIRouter()

@router.post("/properties/", response_description="Add new property", response_model=PropertySchema)
async def create_new_property(property: PropertySchema):
    property_dict = property.model_dump()
    new_property = await PropertyCRUD.create_new_property(property_dict)
    return parse_property_result(new_property)

@router.get("/properties/{city}", response_description="Get properties by city name", response_model=List[PropertySchema])
async def fetch_property_details(city: str):
    properties = await PropertyCRUD.fetch_property_details(city)
    if properties:
        return [parse_property_result(prop) for prop in properties]
    raise HTTPException(status_code=404, detail=f"No properties found in {city}.")

@router.put("/properties/{property_id}", response_description="Update property details", response_model=PropertySchema)
async def update_property_details(property_id: int, property: UpdateProperty):
    update_data = {k: v for k, v in property.model_dump().items() if v is not None}
    updated_property = await PropertyCRUD.update_property_details(property_id, update_data)
    if updated_property:
        return parse_property_result(updated_property)
    raise HTTPException(status_code=404, detail=f"Property with ID {property_id} not found.")
