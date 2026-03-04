from app.services.ai_service import ask_watson
from app.services.source_service import read_source_member
from app.services.db_service import search_database_objects, get_table_columns
import json

def run_demo():
    
    # Fetch Source Code
    library, file, member = "MYLIB", "QRPGLESRC", "DEMO"
    print(f"Reading source: {library}/{file}/{member}...")
    source_content = read_source_member(library, file, member)
    
    # Search for related Database Objects
    print("Searching for related database objects...")
    db_objects = search_database_objects(schema="MYLIB", name="ORDERS")
    db_columns = get_table_columns(schema="MYLIB", table_name="ORDERS")
    
    
    # Construct Enrichment Context
    context = {
        "source": {
            "path": f"{library}/{file}/{member}",
            "content": source_content
        },
        "database_objects": db_objects,
        "table_metadata": {
            "MYLIB/ORDERS": db_columns
        }
    }
  
    # Ask Watson
    prompt = (
        "You are an IBM i modernization expert. Analyze the following RPGLE source code "
        " and its linked database context. If there are vulnerabilites or deprecated/legacy functions, call them out and suggest modern db2/RPGLE refactoring options."
        " Explain how the code interacts with the tables, what columns it filters or updates, and what the business logic appears to do.\n\n"
        f"CONTEXT:\n{json.dumps(context, indent=2)}\n\n"
        "RESPONSE:"
    )
    
    print("\nConnecting to Watsonx...")
    try:
        response = ask_watson(prompt)
        print("-" * 30)
        print("Watson's Analysis:")
        print(response)
        print("-" * 30)
    except Exception as e:
        print("Error connecting to Watsonx:  " + str(e))

if __name__ == "__main__":
    run_demo()
