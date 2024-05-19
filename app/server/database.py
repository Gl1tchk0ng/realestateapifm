import motor.motor_asyncio

MONGO_DETAILS = "mongodb://root:example@localhost:27017/?authSource=admin"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.real_estate_db

cities_collection = database.get_collection("cities")
properties_collection = database.get_collection("properties")
states_collection = database.get_collection("states")


from typing import Any, Dict

def parse_property_result(result: Any) -> Dict[str, Any]:
    return {
        "property_id": result.get("property_id"),
        "property_name": result.get("property_name"),
        "address": result.get("address"),
        "city_name": result.get("city_name"),
        "state": result.get("state")
    }

def parse_city_result(result: Any) -> Dict[str, Any]:
    return {
        "city_id": result.get("city_id"),
        "city_name": result.get("city_name"),
        "state_id": result.get("state_id")
    }

def parse_state_result(result: Any) -> Dict[str, Any]:
    return {
        "state_id": result.get("state_id"),
        "state_name": result.get("state_name")
    }
