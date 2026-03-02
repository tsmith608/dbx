from fastapi import APIRouter, Query
from typing import Optional
from app.services.db_service import search_database_objects

#what FastAPI uses to group endpoints
router = APIRouter()

@router.get("/search")
def search_objects(
    query: Optional[str] = Query(None, description="Search query for object name"),
    schema: Optional[str] = Query(None, description="Schema name filter "),
    obj_type: Optional[str] = Query(None, description="Object type")
    ):


    """
    Search for database objects based on name, schema, and type.
    """

    #pass the web params back down to /db layer
    results = search_database_objects(schema = schema, name = query, obj_type = obj_type)

    #return the results
    return {"status": "success", "count": len(results), "data": results}
    



