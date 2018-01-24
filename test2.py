
# import needed libraries
from datetime import datetime, timedelta
import quandl
import time
import pandas as pd

## yyyy-d-m format
print (time.strftime("%Y-%m-%d"))
today = (time.strftime("%Y-%m-%d"))
yesterday = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
print (yesterday)


# add quandl API key for unrestricted
quandl.ApiConfig.api_key = 'XkzbezVA_z4atB-drwFE'


# get the table for daily stock prices and,
# filter the table for selected tickers, columns within a time range
# set paginate to True because Quandl limits tables API to 10,000 rows per call


data = quandl.get_table('WIKI/PRICES', ticker = ['AAPL', 'CVX', 'RTN', 'MRK'], 
                        qopts = { 'columns': ['ticker', 'date', 'adj_open'] }, 
                        date = { 'gte': '2018-1-1', 'lte': today }, 
                        paginate=True)

new = data.set_index('date')
clean_data = new.pivot(columns='ticker')


print (data)
print (clean_data)
