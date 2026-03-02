# Citation: Ramírez, S. (2024). FastAPI: Modern Python web framework. FastAPI.
# https://fastapi.tiangolo.com/reference/fastapi/

from fastapi import FastAPI
from app.api.v1.endpoints.objects import router as objects_router

#init
app = FastAPI(title="DbX Synapse", version="1.0.0")

#connect to objects API
app.include_router(objects_router, prefix="/api/v1/objects", tags=["Database_Objects"])


#Connection check
@app.get("/")
def read_root():
    return {"status": "online", "service": "DbX Synapse", "message": "DbX Synapse is online"}
