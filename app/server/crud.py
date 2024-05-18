from typing import Any, List, Dict
from server.database import properties_collection

class PropertyCRUD:
    @staticmethod
    async def create_new_property(property: Dict[str, Any]) -> Dict[str, Any]:
        new_property = await properties_collection.insert_one(property)
        created_property = await properties_collection.find_one({"_id": new_property.inserted_id})
        return created_property

    @staticmethod
    async def fetch_property_details(city_name: str) -> List[Dict[str, Any]]:
        properties = []
        async for property in properties_collection.find({"city_name": city_name}):
            properties.append(property)
        return properties

    @staticmethod
    async def update_property_details(property_id: int, update_data: Dict[str, Any]) -> Dict[str, Any]:
        updated_property = await properties_collection.update_one(
            {"property_id": property_id},
            {"$set": update_data}
        )
        if updated_property.modified_count == 1:
            updated_property = await properties_collection.find_one({"property_id": property_id})
            return updated_property
        return None