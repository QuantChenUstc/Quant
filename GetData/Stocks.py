from cmath import nan
from pickletools import long4
from jqdatasdk import *
from pandas import *
import sys
import numpy as np
sys.path.append(__file__[:-17])
from MysqlData.daypriceClass import *
from Database.OperateDB.CommonOperateDB import *
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

def generate_stock_Attribute_column(numStockAttributes, stocks, displayName, abridgeName, startDate, fields):
    ## error
    stockAttributes = [[] for _ in range(numStockAttributes)]
    df = get_price(stocks, end_date=startDate, count=1, frequency='daily', fields = fields, skip_paused=False, fq='pre', panel=False)

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
        if(stockAttributes[indexDict['paused']][index] == False):
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

def generate_stock_Attribute_row(numStockAttributes, stocks, displayName, abridgeName, startDate, fields):
    ## error
    df = get_price(stocks, end_date=startDate, count=1, frequency='daily', fields = fields, skip_paused=False, fq='pre', panel=False)
    isST = get_extras('is_st', stocks, end_date=startDate, count=1, df=False)
    stocksWithAttribute = []
    for i in range(len(df)):
        stockWithAttribute = [0 for _ in range(numStockAttributes)]
        stockWithAttribute[0] = stocks[i]
        stockWithAttribute[1] = displayName[i]
        stockWithAttribute[2] = abridgeName[i]
        stockWithAttribute[3] = startDate
        for attributeIndex in range(4, 15):
            stockWithAttribute[attributeIndex] = df[df['code'] == stocks[i]].at[df[df['code'] == stocks[i]].index.tolist()[0], attributeDict[attributeIndex]]
        
        stockWithAttribute[indexDict['is_st']] = isST[stocks[i]]
        # stockWithAttribute = df.loc[i].tolist()
        if stockWithAttribute[indexDict['paused']] == True and stockWithAttribute[indexDict['open']] == nan:
            continue
        else:
            changeValue = stockWithAttribute[indexDict['close']] - stockWithAttribute[indexDict['pre_close']]
            changeRatio = changeValue/stockWithAttribute[indexDict['pre_close']] * 100
            stockWithAttribute[indexDict['change_price']] = changeValue
            stockWithAttribute[indexDict['change_ratio']] = changeRatio
        stocksWithAttribute.append(stockWithAttribute)
    return stocksWithAttribute

    

def insert_stock_to_mysql(stockAttributes):
    
    return True

def get_stocks_with_insert_mysql(Date, fields, stocks, numStockAttributes):
    df = get_price(stocks, end_date=Date, count=1, frequency='daily', fields = fields, skip_paused=False, fq='pre', panel=False)
    isST = get_extras('is_st', stocks, end_date=Date, count=1, df=False)
    stocksWithAttributes = []
    for i in range(len(df)):

        stockWithAttribute = [0 for _ in range(numStockAttributes)]

        stockWithAttribute[0] = df.iloc[i].at['code']
        stockInfo = get_security_info(stockWithAttribute[0])
        stockWithAttribute[1] = Date
        stockWithAttribute[2] = stockInfo.display_name
        stockWithAttribute[3] = stockInfo.name

        for attributeIndex in range(4, 14):
            stockWithAttribute[attributeIndex] = df.iloc[i].at[attributeDict[attributeIndex]]
        stockWithAttribute[indexDict['paused']] = int(float(df.iloc[i].at['paused']))
        
        if isST[stockWithAttribute[0]][0] == False:
            stockWithAttribute[indexDict['is_st']] = 0
        else:
            stockWithAttribute[indexDict['is_st']] = 1
        
        stockWithAttribute[indexDict['volume']] = int(float(stockWithAttribute[indexDict['volume']]))
        stockWithAttribute[indexDict['money']] = int(float(stockWithAttribute[indexDict['money']]))
        
        if stockWithAttribute[indexDict['paused']] == True and stockWithAttribute[indexDict['open']] == nan:
            continue
        else:
            changeValue = float(stockWithAttribute[indexDict['close']]) - float(stockWithAttribute[indexDict['pre_close']])
            changeRatio = changeValue/float(stockWithAttribute[indexDict['pre_close']]) * 100
            stockWithAttribute[indexDict['change_price']] = np.around(changeValue,2)
            stockWithAttribute[indexDict['change_ratio']] = np.around(changeRatio,2)
        for _ in range(7):
            stockWithAttribute.append(0.0)
        stocksWithAttributes.append(stockWithAttribute)
    
    my_insert_someAttributes(stocksWithAttributes)
    return stocksWithAttributes