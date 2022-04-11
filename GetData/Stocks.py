from jqdatasdk import *
from pandas import *
import sys
sys.path.append(__file__[:-17])
from MysqlData.daypriceClass import Dayprice
auth('15656086889', '@ABC@abc123')

def insertStock(fileName):
    stocks = get_all_securities(['stock'])
    newstocks = stocks.loc[:,['display_name', 'name']]
    newstocks.to_csv(fileName)

def getStock(fileName):
    stocks = read_csv(fileName)
    stocks = stocks.to_numpy()
    n = len(stocks)
    newstocks = []
    for i in range(n):
        newstocks.append(Dayprice(stocks[i][0], stocks[i][1], stocks[i][2]))
    return newstocks