import sqlite3
import os

def init_mock_db():
    db_path = "data/mock/db2_mock.db"
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"Initializing mock database at {db_path}...")
    
    # Create a simple table that our mock connection will route to
    cursor.execute("DROP TABLE IF EXISTS SYSTABLES")
    cursor.execute("""
        CREATE TABLE SYSTABLES (
            TABLE_SCHEMA TEXT,
            TABLE_NAME TEXT,
            TABLE_TYPE TEXT,
            REMARKS TEXT
        )
    """)
    
    # Insert some sample data
    sample_data = [
        ('PRODLIB', 'EMPLOYEE', 'BASE TABLE', 'Employee Master File'),
        ('PRODLIB', 'ORDERS', 'BASE TABLE', 'Customer Orders'),
        ('PRODLIB', 'PRODUCTS', 'BASE TABLE', 'Inventory List'),
        ('QSYS2', 'SYSTABLES', 'VIEW', 'System Table Catalog'),
        ('TESTLIB', 'DEBUG_LOG', 'BASE TABLE', 'Application Debug Logs')
    ]
    
    cursor.executemany("INSERT INTO SYSTABLES VALUES (?, ?, ?, ?)", sample_data)
    
    conn.commit()
    conn.close()
    print("✅ Mock database initialized successfully with sample data.")

if __name__ == "__main__":
    init_mock_db()
