from fastapi import APIRouter, Query
from typing import Optional
from app.services.db_service import search_database_objects, get_table_columns

router = APIRouter()

# Search for database objects based on name, schema, and type.
@router.get("/search")
def search_objects(
    # Allows FastAPI to read the params and validate them 
    # Citation: Ramírez, S. (2024). FastAPI: Modern Python web framework. FastAPI.
    # https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
    query: Optional[str] = Query(None, description="Search query for object name"),
    schema: Optional[str] = Query(None, description="Schema name filter "),
    obj_type: Optional[str] = Query(None, description="Object type")
    ):




    #pass the web params back down to /db layer
    results = search_database_objects(schema, query, obj_type)

    #return the results
    return {"status": "success", "count": len(results), "data": results}

# Get columns for a specific table.
@router.get("/columns")
def get_columns(
    schema: str = Query(..., description="Schema name"),
    table_name: str = Query(..., description="Table name")
    ):
    """
    Get columns for a specific table in a schema.
    """
    results = get_table_columns(schema, table_name)
    return {"status": "success", "count": len(results), "data": results}
    



