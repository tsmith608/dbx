from app.db.connection import get_db_connection
from app.db.queries.catalog import GET_OBJECTS_SEARCH
from app.db.queries.catalog import GET_COLUMNS_FOR_TABLE

#python function to invoke QSYS2
def search_database_objects(schema=None, name=None, obj_type=None):
    
    #search by name if provided
    if name:
        name = f"%{name}%"

    results = []

    #use context manager to ensure connection
    with get_db_connection() as conn:
        cursor = conn.cursor()
    
        #execute query
        cursor.execute(GET_OBJECTS_SEARCH, (schema, schema, name, name, obj_type, obj_type))

        #columns and rows 
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        
        #convert rows to list of dictionaries
        for row in rows:
            results.append(dict(zip(columns, row)))
    
    return results

def get_table_columns(schema: str, table_name: str):
    # get columns for a table
    results = []
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(GET_COLUMNS_FOR_TABLE, (schema, table_name))
        
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        
        for row in rows:
            results.append(dict(zip(columns, row)))
            
    return results


