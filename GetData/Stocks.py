from jqdatasdk import *
from pandas import *
import sys
sys.path.append(__file__[:-17])
from MysqlData.daypriceClass import *
auth('15656086889', '@ABC@abc123')

def insert_stock_to_csv(fileName):
    stocks = get_all_securities(['stock'])
    newstocks = stocks.loc[:,['display_name', 'name']]
    newstocks.to_csv(fileName)

def get_stock(fileName):
    stocks = read_csv(fileName)
    stocks = stocks.to_numpy()
    n = len(stocks)
    newstocksClass = []
    newstocks = []
    displayName = []
    abridgeName = []
    for i in range(n):
        newstocksClass.append(Dayprice(stocks[i][0], stocks[i][1], stocks[i][2]))
        # newstocks.append('\'' + stocks[i][0] + '\'')
        newstocks.append(stocks[i][0])
        displayName.append(stocks[i][1])
        abridgeName.append(stocks[i][2])
    return newstocksClass, newstocks, displayName, abridgeName

def generate_stock_Attribute(numStockAttributes, stocks, displayName, abridgeName, startDate, fields):
    stockAttributes = [[] for _ in range(numStockAttributes)]
    df = get_price(stocks, end_date=startDate, count=1, frequency='daily', fields = fields, skip_paused=True, fq='pre', panel=False)

    stockAttributes[0] = stocks
    stockAttributes[1] = displayName
    stockAttributes[2] = abridgeName
    stockAttributes[3] = list(startDate)

    for attributeIndex in range(4, 15):
        stockAttributes[attributeIndex] = df[attributeDict[attributeIndex]].tolist()

    changeRatio = []
    changePrice = []
    is_st = []

    STarray = get_extras('is_st', stocks, end_date=startDate, count=1, df=False)
    for index in range(len(stocks)):
        is_st.append(STarray[stocks[index]])
    stockAttributes[indexDict['is_st']] = is_st

    for index in range(len(stocks)):
        if(stockAttributes[indexDict['is_st']][index] == False):
            changeValueIndex = stockAttributes[indexDict['close']][index] - stockAttributes[indexDict['pre_close']][index]
            changeRatioIndex = changeValueIndex/stockAttributes[indexDict['pre_close']][index] * 100
            changePrice.append(changeValueIndex)
            changeRatio.append(changeRatioIndex)
        else:
            changePrice.append('nan')
            changeRatio.append('nan')
    stockAttributes[indexDict['change_price']] = changePrice
    stockAttributes[indexDict['change_ratio']] = changeRatio
    
    return stockAttributes

def insert_stock_to_mysql(stockAttributes):
    
    return True