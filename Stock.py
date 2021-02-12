import pandas_datareader.data as stock
from datetime import date,timedelta
import numpy

def GetDetail(Date,StockName,Capital):
    df1=stock.DataReader(StockName[0].upper(),'yahoo',start=Date-timedelta(days=1),end=Date)
    df2=stock.DataReader(StockName[0].upper(),'yahoo',start=date.today()-timedelta(days=1),end=date.today())
    NoOfShares=numpy.float32(Capital)/df1.iloc[-1]['Low']
    return int(NoOfShares*df2.iloc[-1]['High'])
