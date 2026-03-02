import pyodbc

# Debug: See what pyodbc sees
print("Available ODBC Drivers:")
for driver in pyodbc.drivers():
    print(f" - {driver}")
print("-" * 30)

# TEST: IBM i User Profiles have a 10-character MAX limit.
# 'vp25-059-ibmi-9' is 14 characters, which triggers "Key value too long".
# Let's try the shorter one you had before.

uid = "vp25-059-i" # 10 characters exactly
pwd = "dPeT3e61"
system = "172.20.20.38"

drivers_to_try = [
    "{IBM i Access ODBC Driver}",
    "{iSeries Access ODBC Driver}"
]

for driver_name in drivers_to_try:
    print(f"Trying driver: {driver_name} with UID: {uid}")
    conn_str = f"DRIVER={driver_name};SYSTEM={system};UID={uid};PWD={pwd};"

    try:
        conn = pyodbc.connect(conn_str, timeout=5)
        print(f"✅ SUCCESS with {driver_name}!")
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM SYSIBM.SYSDUMMY1")
        print("✅ Query executed successfully!")
        conn.close()
        break
    except Exception as e:
        print(f"❌ Failed with {driver_name}: {e}")
        print("-" * 10)
