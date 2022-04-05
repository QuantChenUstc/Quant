from daypriceClass import Dayprice

test = Dayprice('2022-4-5', '000001.XSGH')
lis = list(test.__dict__.values())
print(lis)