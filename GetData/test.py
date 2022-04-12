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

startDate = '2015-01-30'

stockAttributes = generate_stock_Attribute(numStockAttributes-7, stocks, displayName, abridgeName, startDate, fields)

