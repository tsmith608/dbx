# Citation: Ramírez, S. (2024). FastAPI: Modern Python web framework. FastAPI.
# https://fastapi.tiangolo.com/reference/fastapi/

# python -m uvicorn app.main:app --reload

from fastapi import FastAPI
from app.api.v1.endpoints.objects import router as objects_router
from app.api.v1.endpoints.source import router as source_router

# init
app = FastAPI(title="DbX Synapse", version="1.0.0")

# connect to objects API
app.include_router(objects_router, prefix="/api/v1/objects", tags=["Database_Objects"])

# connect to source code API
# for testing MYLIB/QRPGLESRC/DEMO
app.include_router(source_router, prefix="/api/v1/source", tags=["Source_Code"])



# Connection check
@app.get("/")
def read_root():
    return {"status": "online", "service": "DbX Synapse", "message": "DbX Synapse is online"}
