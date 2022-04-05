from Database.ConnectDB.MySQLPool import UsingMysql
from typing import List
from MysqlData import Dayprice

datatype = List[Dayprice]

def my_insert(datas: datatype):
    n = len(datas)
    with UsingMysql(logTime=True) as um:
        sql = "INSERT INTO day(code, code_date, displayName, abridgeName, openPrice, closePrice, highPrice, lowPrice, prePrice, volume, money, changeRatio, changePrice, highLimit, lowLimit, paused, isST, volumeRatio, ma5, ma10, ma20, ma30, ma60, ma180) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        for i in range(n):
            um.cursor.execute(sql, datas[i].__dict__.values())
    return 0
