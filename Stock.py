import pandas_datareader.data as stock
from datetime import date, datetime,timedelta, timezone
import numpy

def GetDetail(Date,StockName,Capital):
    if Date.weekday()==5:
        Date+=timedelta(days=2)
    elif Date.weekday()==6:
        Date+=timedelta(days=1)
    today=date.today()
    if today.weekday()==0:
        today-=timedelta(days=2)

    df1=stock.DataReader(StockName[0].upper(),'yahoo',start=Date,end=Date)
    df2=stock.DataReader(StockName[0].upper(),'yahoo',start=today,end=today)
    # NoOfShares=numpy.float32(Capital)/df1.iloc[-1]['Low']
    # return int(NoOfShares*df2.iloc[-1]['High'])
    return (numpy.float32(df1.iloc[-1]['Low']),numpy.float32(df2.iloc[-1]['High']))