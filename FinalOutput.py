
# import needed libraries
from datetime import datetime, timedelta
import quandl
import time
import pandas as pd
import scrollphathd
from scrollphathd.fonts import font5x7

## yyyy-d-m format
#print (time.strftime("%Y-%m-%d"))
today = (time.strftime("%Y-%m-%d"))
yesterday = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
#print (yesterday)


# add quandl API key for unrestricted
quandl.ApiConfig.api_key = ''


# get the table for daily stock prices and,
# filter the table for selected tickers, columns within a time range
# set paginate to True because Quandl limits tables API to 10,000 rows per call


data = quandl.get_table('WIKI/PRICES', ticker = ['AAPL', 'CVX', 'RTN', 'MRK'],
                        qopts = { 'columns': ['ticker', 'date', 'adj_open'] },
                        date = { 'gte': yesterday, 'lte': today },
                        paginate=True)

#new = data.set_index('ticker')
#clean_data = new.pivot(columns='ticker')


print(data.head())

#print (clean_data)

#clean_data.to_csv(today+ 'prices.csv', sep ='\t', encoding ='utf-8')
data.to_csv('prices2.csv',sep =' ', encoding = 'utf-8')

newData = pd.read_csv('prices2.csv',skiprows=[0], header=None)

print(newData.head())

stringData = newData.to_string(header=False, index=False, index_names=False).split('\n')

str1 = ''.join(stringData)


print (stringData)
print (str1)
#f = open('text.txt', 'w')
#f.write(stringData)
#f.close()

#this is the portion of the code that is used for the raspberrypi
scrollphathd.rotate(180)

#Set a more eye-friendly default brightness
scrollphathd.set_brightness(0.5)

scrollphathd.write_string(str1, x=0, y=0, font=font5x7, brightness=0.5)

while True:
    scrollphathd.show()
    scrollphathd.scroll()
    time.sleep(0.05)


'''import tkinter as tk

root = tk.Tk()
deli = 100           # milliseconds of delay per character
svar = tk.StringVar()
labl = tk.Label(root, textvariable=svar, height=10)

def shif():
    shif.msg = shif.msg[1:] + shif.msg[0]
    svar.set(shif.msg)
    root.after(deli, shif)

shif.msg = str1
shif()
labl.pack()
root.mainloop()'''
