"""
Executed by destination, Run the script has been generate.
Table should be dropped if it exists.
"""
from pathlib import Path
import os
import pyodbc
import re
import argparse
from create_table import CREATE_POI_DATA_TABLE, CREATE_PARKING_ADJUST_TABLE, CREATE_MASTER_TABLE

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
    
def insert_all_county(table):
        
    # first, drop table manually
    # ...
    if table == 'poi_data':
        print("table is poi_data")
        cur.execute(CREATE_POI_DATA_TABLE)
    elif table == 'parking_adjust':
        print("table is parking_adjust")
        cur.execute(CREATE_PARKING_ADJUST_TABLE)
    elif table == 'master':
        print("table is master")
        cur.execute(CREATE_MASTER_TABLE)
    file_path = Path(f'C:\\sql_scripts\\{table}_python')
    
    cur.execute(f"SET IDENTITY_INSERT [dbo].[{table}] ON")
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
    cur.execute(f"SET IDENTITY_INSERT [dbo].[{table}] OFF")
    

parser = argparse.ArgumentParser()
parser.add_argument("arg1", help="1 argument, [TABLE_NAME]")
args = parser.parse_args()

insert_all_county(args.arg1)