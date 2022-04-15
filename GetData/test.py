from jqdatasdk import *
import sys
sys.path.append(__file__[:-15])
sys.path.append("..")
from Stocks import *
from MysqlData.daypriceClass import Dayprice
#import MysqlData

auth('15656086889', '@ABC@abc123')

## pull stock from jq
csvFile = __file__[:-7] + 'stocks.csv'
# insert_stock_to_csv(csvFile)
stocksClass, stocks, displayName, abridgeName = get_stock(csvFile)

numStockAttributes = len(indexDict)

fields = ['open','close','low','high','volume','money','factor','high_limit','low_limit','avg','pre_close','paused']
print("start to get price")

startDate = '2022-04-14'

#stockAttributes = generate_stock_Attribute_row(numStockAttributes-7, stocks, displayName, abridgeName, startDate, fields)

#print(stockAttributes[0])
sas = ['000001.XSHE','000002.XSHE']
testv = get_price(sas, end_date=startDate, count=1, frequency='daily', fields = fields, skip_paused=False, fq='pre', panel=False)
#print(testv)
aa = testv[testv['code'] == '000001.XSHE'].loc[0].tolist()
# print(aa)
#isST = get_extras('is_st', sas, end_date=startDate, count=1, df=False)
#print(isST[sas[0]][0])
stocksa = get_stocks_with_insert_mysql(startDate, fields, sas, numStockAttributes-7)
print(stocksa[1])