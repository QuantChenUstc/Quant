from daypriceClass import Dayprice
import sys
sys.path.append("..")
from Database import ConnectDB
from Database.OperateDB import CommonOperateDB


test = Dayprice('000001.XSGH', '2022-4-5')
test.set_param("贵州茅台", "gzmt", "1234.12", "1250.24", "1260.13", "1230.45", "1234.10", 1234567, 1231145, "1.23", "34.25", "1342.12", "1123.63", 0, 0, "43.21")
test.set_ma("1241.23", "4332.23", "4212.52", "2412.63", "3214.53", "2314.53")
print(test.__dict__)
lis = list(test.__dict__.values())
print(lis)

datas = []
datas.append(lis)
CommonOperateDB.my_insert(datas)