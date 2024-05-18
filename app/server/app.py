from fastapi import FastAPI
from server.routes.property_routes import router as property_router

app = FastAPI()

app.include_router(property_router, prefix="/api")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the Real Estate API!"}
