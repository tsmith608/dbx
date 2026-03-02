from fastapi import FastAPI
from app.api.v1.endpoints import router as api_router

app = FastAPI(title="Gandr Analyzer API")

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to Gandr Analyzer API"}
