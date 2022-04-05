import sys
sys.path.append("..")
from Database.ConnectDB.MySQLPool import UsingMysql
from typing import List
import pymysql

test = ['000001.XSGH', '2022-4-5', '贵州茅台', 'gzmt', '1234.12', '1250.24', '1260.13', '1230.45', '1234.10', 1234567, 1231145, '1.23', '34.25', '1342.12', '1123.63', 0, 0, '43.21', '1241.23', '4332.23', '4212.52', '2412.63', '3214.53', '2314.53']
def my_insert(datas: list):
    n = len(datas)
    with UsingMysql(logTime=True) as um:
        sql = "INSERT INTO day(code, code_date, display_name, abridge_name, open_price, close_price, high_price, low_price, pre_close, volume, allmoney, change_ratio, change_price, high_limit, low_limit, paused, is_st, volume_ratio, ma5, ma10, ma20, ma30, ma60, ma180) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        for i in range(n):
            try:
                um._cursor.execute(sql, datas[i])
                um._conn.commit()
            except Exception as e:
                print("fail to insert into db\n")
                um._conn.rollback()
    return 0

if __name__ == "__main__":
    my_insert([1])
    
    '''
    conn = pymysql.connect(host="localhost",
                           port=3306,
                           user="root",
                           password="root",
                           database="data_day",
                           charset="utf8")
    cursor = conn.cursor()
    sql = "INSERT INTO day(code, code_date, display_name, abridge_name, open_price, close_price, high_price, low_price, pre_close, volume, allmoney, change_ratio, change_price, high_limit, low_limit, paused, is_st, volume_ratio, ma5, ma10, ma20, ma30, ma60, ma180) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    print(sql)
    try:
        cursor.execute(sql, test)
        conn.commit()
    except Exception as e:
        print("sd")
    finally:
        cursor.close()
        conn.close()
    '''