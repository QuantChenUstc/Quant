from tkinter import SEL_LAST


class Dayprice:
    '''
    date = ""
    code = ""
    displayName = ""
    abridgeName = ""
    openPrice = 0.0
    closePrice = 0.0
    highPrice = 0.0
    lowPrice = 0.0
    prePrice = 0.0
    volume = 0
    money = 0
    changeRatio = 0.0
    changePrice = 0.0
    highLimit = 0.0
    lowLimit = 0.0
    paused = 0
    isST = 0
    volumeRatio = 0.0
    ma5 = 0.0
    ma10 = 0.0
    ma20 = 0.0
    ma30 = 0.0
    ma60 = 0.0
    ma180 = 0.0
    '''
    def __init__(self, code : str, displayName : str, abridgeName : str):
        self.code = code
        self.displayName = displayName
        self.abridgeName = abridgeName
        
        
    def set_param(self, date, openPrice, closePrice, highPrice, lowPrice, prePrice, volume, money, highLimit, lowLimit, paused):
        self.date = date
        self.openPrice = openPrice
        self.closePrice = closePrice
        self.highPrice = highPrice
        self.lowPrice = lowPrice
        self.prePrice = prePrice
        self.volume = volume
        self.money = money
        self.highLimit = highLimit
        self.lowLimit = lowLimit
        self.paused = paused
        
    def set_change(self, changeRatio, changePrice):
        self.changeRatio = changeRatio
        self.changePrice = changePrice
    
    def set_volumeRatio(self, volumeRatio):
        self.volumeRatio = volumeRatio

    def set_isST(self, isST):
        self.isST = isST
 
    def set_ma(self, ma5, ma10, ma20, ma30, ma60, ma180):
        self.ma5 = ma5
        self.ma10 = ma10
        self.ma20 = ma20
        self.ma30 = ma30
        self.ma60 = ma60
        self.ma180 = ma180
    
    def show(self):
        print(self.code + " " + self.displayName + " " + self.abridgeName)
    

indexDict = {'code': 0, 'date': 1, 
            'display_name': 2, 'name': 3,
            'open': 4, 'close': 5,
            'high': 6, 'low': 7, 
            'pre_close': 8, 'avg': 9, 
            'volume': 10, 'money': 11, 
            'high_limit': 12, 'low_limit': 13,
            'paused': 14,
            'change_ratio': 15, 'change_price': 16,
            'is_st': 17, 
            'volume_ratio': 18,
            'ma5': 19, 'ma10': 20, 'ma20': 21, 'ma30': 22, 'ma60': 23, 'ma180': 24}
attributeDict = {0: 'code', 1: 'date', 
            2: 'display_name', 3: 'name',
            4: 'open', 5: 'close',
            6: 'high', 7: 'low', 
            8: 'pre_close', 9: 'avg', 
            10: 'volume', 11: 'money', 
            12: 'high_limit', 13: 'low_limit', 
            14: 'paused',
            15: 'change_ratio', 16: 'change_price',
            17: 'is_st', 
            18: 'volume_ratio', 
            19: 'ma5', 20: 'ma10', 21: 'ma20', 22: 'ma30', 23: 'ma60', 24: 'ma180'}