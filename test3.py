import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import time


style.use('ggplot')

start = dt.datetime(2018, 1, 1)
end = dt.datetime(2018, 1, 19)

df = web.DataReader('TSLA', "yahoo", start, end)


print(df.head())
