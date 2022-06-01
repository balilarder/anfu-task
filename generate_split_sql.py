# all_county =  [
#     "台北市",
#     "台中市",
#     "台南市",
#     "高雄市",
#     "新北市",
#     "宜蘭縣",
#     "桃園市",
#     "基隆市",
#     "嘉義市",
#     "新竹縣",
#     "苗栗縣",
#     "南投縣",
#     "彰化縣",
#     "新竹市",
#     "雲林縣",
#     "嘉義縣",
#     "屏東縣",
#     "花蓮縣",
#     "台東縣",
#     "金門縣",
#     "澎湖縣",
#     "連江縣"
# ]
all_county = {
    "台中市": "TaichungCity",
    "台北市": "TaipeiCity",
    "台東縣": "TaitungCounty",
    "台南市": "TainanCity",
    "宜蘭縣": "YilanCounty",
    "花蓮縣": "HualienCounty",
    "金門縣": "KinmenCounty",
    "南投縣": "NantouCounty",
    "屏東縣": "PingtungCounty",
    "苗栗縣": "MiaoliCounty",
    "桃園市": "TaoyuanCity",
    "高雄市": "KaohsiungCity",
    "基隆市": "KeelungCity",
    "連江縣": "LienchiangCounty",
    "雲林縣": "YunlinCounty",
    "新北市": "NewTaipeiCity",
    "新竹市": "HsinchuCity",
    "新竹縣": "HsinchuCounty",
    "嘉義市": "ChiayiCity",
    "嘉義縣": "ChiayiCounty",
    "彰化縣": "ChanghuaCounty",
    "澎湖縣": "PenghuCounty",
}   
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


def generate_script(county, table, base_path):

    sql_query = pd.read_sql_query(f"SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table}'", conn)
    df = pd.DataFrame(sql_query)
    df.drop(df[df.DATA_TYPE == "geometry"].index, inplace=True)  # remove geom column because pyodbc not support
    column_name = df['COLUMN_NAME'].tolist()
    data_type = df['DATA_TYPE'].to_list()
    insert_table_name = f"{table}"
    insert_query = f"INSERT [dbo].[{insert_table_name}] ("
    for cn in column_name[:-1]:
        insert_query += f"[{cn}], "
    insert_query += f"[{column_name[-1]}]) VALUES "
    # print(f"column names: {column_name}")
    # print(data_type)  # ["int"-int, "varchar"-str, "decimal"-decimal.Decimal, "datetime"-datetime.datetime]
    for col_name, dtype in zip(column_name, data_type):
        print(col_name, dtype)
    
    def convert_format(col_names) -> str:
        temp = [f"[{col_name}]" for col_name in col_names]
        return ",".join(temp)
    column_names_need = convert_format(column_name)
    
    # query_str = f"select * from moi_avm.dbo.{table} where county = '{county}'"
    # query_str = f"select top 100 [id],[county],[form_no],[town],[trans_type],[raw_address] from moi_avm.dbo.{table} where county = '{county}'"
    # query_str = f"select top 100000 * from moi_avm.dbo.{table} where county = '{county}'"
    query_str = f"select {column_names_need} from moi_avm.dbo.{table} where county = '{county}'"
    query_result = cur.execute(query_str)
    
    X = 40000
    # X = 4000
    # X = 28
    i = 0
    for r in query_result:
        batch = (i // X) + 1
        sql_file_name = f"{table}.{all_county[county]}{batch}.sql"
        if not Path(base_path + sql_file_name).exists():
            Path(base_path + sql_file_name).touch()
            with open(base_path + sql_file_name, 'w', encoding='ANSI') as f:
                f.write(f"USE [moi_avm]\n")
                f.write(f"SET ANSI_NULLS ON\n")
                f.write(f"SET QUOTED_IDENTIFIER ON\n")
                f.write(f"SET IDENTITY_INSERT [dbo].[{table}] ON\n")
        with open(base_path + sql_file_name, 'a', encoding='ANSI') as f:
            # fill in data
            data = "("
            for col_cnt in range(len(data_type)):
                # print(f"data: {r[col_cnt]}, type {type(r[col_cnt])}")
                
                if data_type[col_cnt] == "int":
                    if r[col_cnt] == None:
                        data += "NULL, "
                    else:
                        data += f"{r[col_cnt]}, "
                elif data_type[col_cnt] == "varchar" or data_type[col_cnt] == "nvarchar":
                    # a = r[col_cnt].replace("None", "")
                    # data += f"N'{r[col_cnt]}', "
                    data += "N'{}', ".format(str(r[col_cnt]).replace("None", ""))
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

def create_table_command(table, base_path):
    import create_table
    if table == 'poi_data':
        command = create_table.CREATE_POI_DATA_TABLE
    elif table == 'parking_adjust':
        command = create_table.CREATE_PARKING_ADJUST_TABLE
    elif table == 'master':
        command = create_table.CREATE_MASTER_TABLE
    else:
        return
    with open(base_path + 'create_table.sql', 'w', encoding='ANSI') as f:
        f.write(command)
        
# def set_identity_insert_off(table, base_path):
#     with open(base_path + 'set_identity_insert_off.sql', 'w', encoding='ANSI') as f:
#         f.write(f"SET IDENTITY_INSERT [dbo].[{table}] OFF")


def combine_to_bat(table, base_path):
    files = list(Path(base_path).glob('*.sql'))
    print(f"files are")
    files = [f for f in files if table in str(f.name)]
    
    # 為每個.sql 最後設定 identity OFF
    for file in files:
        with open(file, 'a', encoding='ANSI') as f:
            f.write(f"SET IDENTITY_INSERT [dbo].[{table}] OFF\n")
            
    with open(base_path + table + '.bat', 'w', encoding='ANSI') as f:
        f.write(f"sqlcmd -i {base_path}create_table.sql\n")
        # others sql
        for file in files:
            f.write(f"sqlcmd -i {str(file)}\n")
        

# main
# for county in all_county:
#     generate_script_poi_data(county, base_path)

parser = argparse.ArgumentParser()
parser.add_argument("arg1", help="1 argument, [TABLE_NAME]")
args = parser.parse_args()

# base_path = f"C:\\tmp\\20220406_updateDB\\{args.arg1}_python\\"
base_path = f"D:\setup_20220531\{args.arg1}\\"
for i in Path(base_path).glob('*.sql'):
    i.unlink()

for county in all_county.keys():
    print(f"generate {county} sql file")
    generate_script(county, args.arg1, base_path)

create_table_command(args.arg1, base_path)
# set_identity_insert_off(args.arg1, base_path)

# # combine all .sql to a .bat
combine_to_bat(args.arg1, base_path)
