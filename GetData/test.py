from jqdatasdk import *
import sys
sys.path.append(__file__[:-15])
sys.path.append("..")
from Stocks import *
from MysqlData.daypriceClass import Dayprice
#import MysqlData

auth('15656086889', '@ABC@abc123')

csvFile = __file__[:-7] + 'stocks.csv'
# insertStock(csvFile)
stocks = getStock(csvFile)

fields = ['open','close','low','high','volume','money','factor','high_limit','low_limit','avg','pre_close','paused']





