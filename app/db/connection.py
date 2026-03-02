import pyodbc
import sqlite3
import os
from app.core.config import settings
from contextlib import contextmanager

# Used Gemini to make this class use a mock db until IMB access is resolved
# Citation: Gemini 3 Flash
class MockCursor:
    """
    A wrapper for the SQLite cursor that translates some IBM i SQL 
    syntax (like QSYS2 schema and FETCH FIRST) into SQLite syntax.
    """
    def __init__(self, cursor):
        self.cursor = cursor
    
    def execute(self, sql, params=()):
        # Handle the QSYS2 schema prefix
        sql = sql.replace("QSYS2.", "")
        # Handle "FETCH FIRST X ROWS ONLY" -> "LIMIT X"
        if "FETCH FIRST" in sql:
            parts = sql.split("FETCH FIRST")
            limit_part = parts[1].split("ROWS ONLY")[0].strip()
            sql = parts[0] + f"LIMIT {limit_part}"
        
        return self.cursor.execute(sql, params)

    def __getattr__(self, name):
        return getattr(self.cursor, name)

class MockConnection:
    """Wraps the sqlite connection to return our MockCursor."""
    def __init__(self, conn):
        self.conn = conn
    
    def cursor(self):
        return MockCursor(self.conn.cursor())

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def __getattr__(self, name):
        return getattr(self.conn, name)

@contextmanager
def get_db_connection():
    if settings.USE_MOCK:
        os.makedirs(os.path.dirname(settings.MOCK_DB_PATH), exist_ok=True)
        conn = sqlite3.connect(settings.MOCK_DB_PATH)
        conn.row_factory = sqlite3.Row
        try:
            yield MockConnection(conn)
        finally:
            # MockConnection handles closure if used in 'with', 
            # but we ensure it here for safety.
            pass
        return


    #construct connection string
    conn_str = (
        f"DRIVER={settings.DB_DRIVER};"
        f"SYSTEM={settings.IBMI_HOST};"
        f"UID={settings.IBMI_USER};"
        f"PWD={settings.IBMI_PASSWORD};"
        f"DATABASE={settings.IBMI_DATABASE};"
        f"PORT={settings.IBMI_PORT};"
        )

    conn = None
    #connect to the database
    try:
        print( "Connecting to " + settings.IBMI_HOST + "..." )
        conn = pyodbc.connect(conn_str, timeout=10)
        yield conn
    except Exception as e:
        print( "Failed to connect to " + settings.IBMI_HOST + ": " + str(e) )
        raise e
    finally:
        if conn:
            conn.close()
            print( "Connection closed" )

    