"""
Executed by destination, Run the script has been generate.
Table should be dropped if it exists.
"""
from pathlib import Path
import os
import pyodbc
import re
from create_table import CREATE_POI_DATA_TABLE

# DB config
server = os.getenv('AVM_DB_HOST')
database = os.getenv('AVM_DB_NAME')
username = os.getenv('AVM_DB_USER')
password = os.getenv('AVM_DB_PASSWORD')

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER='+server+';'
    'DATABASE='+database+';'
    'UID='+username+';'
    'PWD='+ password)
cur = conn.cursor()

def insert_all_poi_data_sql():
    # first, drop table manually    
    cur.execute(CREATE_POI_DATA_TABLE)
    cur.execute("SET IDENTITY_INSERT [dbo].[poi_data] ON")
    file_path = Path('C:\\sql_scripts\\poi_data_python')
    for sql_file in file_path.glob('*.sql'):
        print(sql_file)
        
        with open(sql_file, encoding='UTF-8') as fp:
            count = 0
            Lines = fp.readlines()
            for line in Lines:
                count += 1
                query = line.strip()
                print(sql_file, count)
                try:
                    cur.execute(query)
                    conn.commit()
                except Exception as e:
                    print(f"{sql_file} line: {count} systax error")
    cur.execute("SET IDENTITY_INSERT [dbo].[poi_data] OFF")
    


insert_all_poi_data_sql()