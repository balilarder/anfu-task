all_county =  [
    "台北市",
    "台中市",
    "台南市",
    "高雄市",
    "新北市",
    "宜蘭縣",
    "桃園市",
    "基隆市",
    "嘉義市",
    "新竹縣",
    "苗栗縣",
    "南投縣",
    "彰化縣",
    "新竹市",
    "雲林縣",
    "嘉義縣",
    "屏東縣",
    "花蓮縣",
    "台東縣",
    "金門縣",
    "澎湖縣",
    "連江縣"
]   
"""
Executed by source, generate script from localhost
"""

from itertools import count
from pathlib import Path
import os
import pyodbc
import pandas as pd
import argparse

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

# deprecated
def generate_script_poi_data(county, base_path):
    query_str = f"select top 100 * from moi_avm.dbo.poi_data where county = '{county}'"
    query_result = cur.execute(query_str)
    
    poi_data_schema = "INSERT [dbo].[poi_data] ([id], [county], [data_catagory], [form_no], [t_station_min_distance_count], " \
        + "[t_station_line_distance_count], [t_station_min_distance_name], [t_station_line_distance_name], [t_station_min_distance], " \
        + "[t_station_line_distance], [junction_min_distance_count], [junction_line_distance_count], [junction_min_distance_name], " \
        + "[junction_line_distance_name], [junction_min_distance], [junction_line_distance], [school_min_distance_count], [school_line_distance_count], " \
        + "[school_min_distance_name], [school_line_distance_name], [school_min_distance], [school_line_distance], [service_facilities_min_distance_count], " \
        + "[service_facilities_line_distance_count], [service_facilities_min_distance_name], [service_facilities_line_distance_name], " \
        + "[service_facilities_min_distance], [service_facilities_line_distance], [market_min_distance_count], [market_line_distance_count], " \
        + "[market_min_distance_name], [market_line_distance_name], [market_min_distance], [market_line_distance], [park_min_distance_count], " \
        + "[park_line_distance_count], [park_min_distance_name], [park_line_distance_name], [park_min_distance], [park_line_distance], " \
        + "[station_min_distance_count], [station_line_distance_count], [station_min_distance_name], [station_line_distance_name], " \
        + "[station_min_distance], [station_line_distance], [parking_min_distance_count], [parking_line_distance_count], [parking_min_distance_name], " \
        + "[parking_line_distance_name], [parking_min_distance], [parking_line_distance], [bad_facilities_min_distance_count], " \
        + "[bad_facilities_line_distance_count], [bad_facilities_min_distance_name], [bad_facilities_line_distance_name], [bad_facilities_min_distance], " \
        + "[bad_facilities_line_distance], [created_at], [updated_at]) VALUES " 
    num_fields = len(cur.description) # 60 for poi
    data_type = [
        'int','str','str','str','int','int','str','str','decimal.Decimal',
        'decimal.Decimal','int','int','str','str','decimal.Decimal','decimal.Decimal',
        'int','int','str','str','decimal.Decimal','decimal.Decimal','int','int','str',
        'str','decimal.Decimal','decimal.Decimal','int','int','str','str','decimal.Decimal',
        'decimal.Decimal','int','int','str','str','decimal.Decimal','decimal.Decimal',
        'int','int','str','str','decimal.Decimal','decimal.Decimal','int','int','str',
        'str','decimal.Decimal','decimal.Decimal','int','int','str','str','decimal.Decimal',
        'decimal.Decimal','datetime.datetime','datetime.datetime'
    ]    # int: 19, str: 21, decimal: 18, datetime: 2
    X = 200000
    i = 0
    for r in query_result:
        batch = (i // X) + 1
        sql_file_name = f"{county}{batch}.sql"
        if not Path(base_path + sql_file_name).exists():
            Path(base_path + sql_file_name).touch()
        with open(base_path + sql_file_name, 'a', encoding='UTF-8') as f:
            # fill in data
            data = "("
            for col_cnt in range(num_fields):
                # print(data_type[col_cnt], type(data_type[col_cnt]))
                print(f"data: {r[col_cnt]}, type {type(r[col_cnt])}")
                
                if data_type[col_cnt] == "int":
                    data += f"{r[col_cnt]}, "
                elif data_type[col_cnt] == "str":
                    data += f"N'{r[col_cnt]}', "
                elif data_type[col_cnt] == "decimal.Decimal":
                    # if not r[col_cnt]:
                    if r[col_cnt] is None:
                        print(f"no cast decimal, data is {r[col_cnt]}->NULL")
                        data += "NULL, "
                        continue
                    data += f"CAST({r[col_cnt]} AS Decimal(18, 2)), "
                elif data_type[col_cnt] == "datetime.datetime":
                    # try1
                    # print(f"split datetime")
                    # print(str(r[col_cnt]).split(' '))
                    part1, part2 = str(r[col_cnt]).split(' ')
                    data += f"CAST(N'{part1}T{part2[:-3]}' AS DateTime), "
                    

            data = data[:-2] + ')'
            f.write(f"{poi_data_schema + data}\n")    
        print(f"writing {i} th query... into {sql_file_name}")
        i += 1
    print(f"total {i} result")

def generate_script(county, table, base_path):

    sql_query = pd.read_sql_query(f"SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table}'", conn)
    df = pd.DataFrame(sql_query)
    column_name = df['COLUMN_NAME'].tolist()
    data_type = df['DATA_TYPE'].to_list()
    
    insert_query = f"INSERT [dbo].[{table}] ("
    for cn in column_name[:-1]:
        insert_query += f"[{cn}], "
    insert_query += f"[{column_name[-1]}]) VALUES "
    print(column_name)
    print(data_type)  # ["int"-int, "varchar"-str, "decimal"-decimal.Decimal, "datetime"-datetime.datetime]

    query_str = f"select top 10000 * from moi_avm.dbo.{table} where county = '{county}'"
    query_result = cur.execute(query_str)
    
    X = 200000
    i = 0
    for r in query_result:
        batch = (i // X) + 1
        sql_file_name = f"{county}{batch}.sql"
        if not Path(base_path + sql_file_name).exists():
            Path(base_path + sql_file_name).touch()
        with open(base_path + sql_file_name, 'a', encoding='UTF-8') as f:
            # fill in data
            data = "("
            for col_cnt in range(len(data_type)):
                # print(f"data: {r[col_cnt]}, type {type(r[col_cnt])}")
                
                if data_type[col_cnt] == "int":
                    data += f"{r[col_cnt]}, "
                elif data_type[col_cnt] == "varchar":
                    data += f"N'{r[col_cnt]}', "
                elif data_type[col_cnt] == "decimal":
                    # if not r[col_cnt]:
                    if r[col_cnt] is None:
                        print(f"no cast decimal, data is {r[col_cnt]}->NULL")
                        data += "NULL, "
                        continue
                    data += f"CAST({r[col_cnt]} AS Decimal(18, 2)), "
                elif data_type[col_cnt] == "datetime":
                    format_date = r[col_cnt].strftime("%Y-%m-%dT%H:%M:%S")
                    data += f"CAST(N'{format_date}' AS DateTime), "
            data = data[:-2] + ')'
            f.write(f"{insert_query + data}\n")    
        print(f"writing {i} th query... into {sql_file_name}")
        i += 1
    print(f"total {i} result")

# main
# for county in all_county:
#     generate_script_poi_data(county, base_path)

parser = argparse.ArgumentParser()
parser.add_argument("arg1", help="1 argument, [TABLE_NAME]")
args = parser.parse_args()

base_path = f"C:\\tmp\\20220406_updateDB\\{args.arg1}_python\\"
for i in Path(base_path).glob('*.sql'):
    i.unlink()

for county in all_county:
    generate_script(county, args.arg1, base_path)