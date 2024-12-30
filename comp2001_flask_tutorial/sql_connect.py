#sql_connect.py
import pyodbc #driver 

#databse details
server = 'DIST-6-505.uopnet.plymouth.ac.uk'
database = 'COMP2001_MFish'
username = 'MFish'
password = 'UjkN272*'
driver =  '{ODBC Driver 17 for SQL Server}'

#conenction details
conn_str = (
    f'DRIVER={driver};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
    'Encrypt=Yes;'
    'TrustServerCertificate=Yes;'
    'Connection Timeout=30;'
    'Trusted_Connection=No'
)

#connects the driver with connection details
conn = pyodbc.connect(conn_str)

#execute sql commands
cursor = conn.cursor()

columns = [
    'id INT IDENTITY(1,1) PRIMARY KEY',
    'lname VARCHAR(25) UNIQUE',
    'fname VARCHAR(25)',
    'timestamp DATETIME',
    ]

create_table_cmd = f"CREATE TABLE person ({','.join(columns)})"
cursor.execute(create_table_cmd)
cursor.commit()

people = [
    "'Grace', 'Hopper', '2024-11-19 16:15:10'",
    "'Tim', 'Berners-Lee', '2024-11-19 16:15:13'",
    "'Ada', 'Lovelace', '2024-11-19 16:15:27'",
    ]

for person_data in people:
    insert_cmd = f"INSERT INTO person VALUES ({person_data})"
    cursor.execute(insert_cmd)

cursor.commit()

