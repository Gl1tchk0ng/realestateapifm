from typing import Any, List, Dict, Optional
from server.database import properties_collection

class PropertyCRUD:
    @staticmethod
    async def create_new_property(property: Dict[str, Any]) -> Dict[str, Any]:
        new_property = await properties_collection.insert_one(property)
        created_property = await properties_collection.find_one({"_id": new_property.inserted_id})
        return created_property

    @staticmethod
    async def fetch_property_details(city: str) -> List[Dict[str, Any]]:
        properties = []
        async for property in properties_collection.find({"city": city}):
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
    
    @staticmethod
    async def find_cities_by_state(state: Optional[str] = None) -> List[str]:
        if not state:
            return []

        query = {"state": state}
        cities = set()
        async for property in properties_collection.find(query):
            cities.add(property["city"])
        return list(cities)
    
    @staticmethod
    async def find_similar_properties(property_id: int) -> List[Dict[str, Any]]:
        property = await properties_collection.find_one({"property_id": property_id})
        if not property:
            return []
        city = property.get("city")
        if not city:
            return []

        similar_properties = []
        async for prop in properties_collection.find({"city": city}):
            if prop["property_id"] != property_id:
                similar_properties.append(prop)
        return similar_properties