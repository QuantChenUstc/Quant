from tkinter import SEL_LAST


class dayprice:
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

    def __init__(self, date, code):
        self.date = date
        self.code = code

    def set_param(self, displayName, abridgeName, openPrice, closePrice, highPrice, lowPrice, prePrice, volume, money, changeRatio, changePrice, highLimit, lowLimit, paused, isST, volumeRatio, ma5, ma10, ma20, ma30, ma60, ma180):
        self.displayName = displayName
        self.abridgeName = abridgeName
        self.openPrice = openPrice
        self.closePrice = closePrice
        self.highPrice = highPrice
        self.lowPrice = lowPrice
        self.prePrice = prePrice
        self.volume = volume
        self.money = money
        self.changeRatio = changeRatio
        self.changePrice = changePrice
        self.highLimit = highLimit
        self.lowLimit = lowLimit
        self.paused = paused
        self.isST = isST
        self.volumeRatio = volumeRatio
        self.ma5 = ma5
        self.ma10 = ma10
        self.ma20 = ma20
        self.ma30 = ma30
        self.ma60 = ma60
        self.ma180 = ma180