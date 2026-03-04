import sqlite3
import os

def init_mock_db():
    db_path = "data/mock/db2_mock.db"
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"Initializing mock database at {db_path}...")
    
    # Create SYSTABLES
    cursor.execute("DROP TABLE IF EXISTS SYSTABLES")
    cursor.execute("""
        CREATE TABLE SYSTABLES (
            TABLE_SCHEMA TEXT,
            TABLE_NAME TEXT,
            TABLE_TYPE TEXT,
            REMARKS TEXT
        )
    """)
    
    # Create SYSCOLUMNS
    cursor.execute("DROP TABLE IF EXISTS SYSCOLUMNS")
    cursor.execute("""
        CREATE TABLE SYSCOLUMNS (
            TABLE_SCHEMA TEXT,
            TABLE_NAME TEXT,
            COLUMN_NAME TEXT,
            DATA_TYPE TEXT,
            LENGTH INTEGER,
            COLUMN_TEXT TEXT,
            IS_IDENTITY TEXT DEFAULT 'N'
        )
    """)
    
    # Insert Tables
    tables = [
        ('MYLIB', 'CUSTOMERS', 'BASE TABLE', 'Customer Master File'),
        ('MYLIB', 'ORDERS', 'BASE TABLE', 'Order Header Records'),
        ('MYLIB', 'ORDDETAILS', 'BASE TABLE', 'Order Line Items'),
        ('PRODLIB', 'PRODUCTS', 'BASE TABLE', 'Inventory Item Master'),
        ('SALESLIB', 'REGIONS', 'BASE TABLE', 'Regional Sales Offices'),
        ('SALESLIB', 'SALESREP', 'BASE TABLE', 'Sales Representative List'),
        ('QSYS2', 'SYSTABLES', 'VIEW', 'System Table Catalog'),
        ('QSYS2', 'SYSCOLUMNS', 'VIEW', 'System Column Catalog'),
        ('TESTLIB', 'DEBUG_LOG', 'BASE TABLE', 'Application Debug Logs')
    ]
    
    cursor.executemany("INSERT INTO SYSTABLES VALUES (?, ?, ?, ?)", tables)

    # Insert Columns (Sample for CUSTOMERS and ORDERS)
    columns = [
        ('MYLIB', 'CUSTOMERS', 'CUSTID', 'INTEGER', 9, 'Customer ID Number', 'Y'),
        ('MYLIB', 'CUSTOMERS', 'CUSTNAME', 'VARCHAR', 100, 'Customer Legal Name', 'N'),
        ('MYLIB', 'CUSTOMERS', 'CUSTTYPE', 'CHAR', 2, 'Customer Category Code', 'N'),
        ('MYLIB', 'ORDERS', 'ORDERID', 'INTEGER', 9, 'Unique Order Number', 'Y'),
        ('MYLIB', 'ORDERS', 'CUSTID', 'INTEGER', 9, 'Customer ID Link', 'N'),
        ('MYLIB', 'ORDERS', 'ORDDATE', 'DATE', 10, 'Date Order Placed', 'N'),
        ('MYLIB', 'ORDERS', 'ORDSTS', 'CHAR', 1, 'Order Status Flag', 'N')
    ]
    
    cursor.executemany("INSERT INTO SYSCOLUMNS VALUES (?, ?, ?, ?, ?, ?, ?)", columns)

    # Create the actual ORDERS table and insert data for the demo
    cursor.execute("DROP TABLE IF EXISTS ORDERS")
    cursor.execute("""
        CREATE TABLE ORDERS (
            ORDERID INTEGER PRIMARY KEY,
            CUSTID INTEGER,
            ORDDATE DATE,
            ORDSTS CHAR(1)
        )
    """)
    
    order_data = [
        (1001, 500, '2026-03-01', 'P'),  # P = Pending (will be Shippped by RPG)
        (1002, 501, '2026-03-02', 'S'),  # S = Shipped
        (1003, 502, '2026-03-03', 'P')   # Another Pending
    ]
    cursor.executemany("INSERT INTO ORDERS (ORDERID, CUSTID, ORDDATE, ORDSTS) VALUES (?, ?, ?, ?)", order_data)
    
    conn.commit()
    conn.close()
    print("✅ Mock database initialized successfully with linked data in MYLIB.")

if __name__ == "__main__":
    init_mock_db()
