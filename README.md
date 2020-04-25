# headlesspi

## Goal: The purpose of this is to be able to access the raspberry pi through SSH, and avoid using the Gui interface of the Pi Zero W. 

* The Pi Zero W is great, but is underpowered to the point utilizing the GUI interface for the OS is unrealistic and incredibly slow. 
* In this Project I created a stock ticker that pull data using quandl api

## Tools:
  * Python
    * Numpy
    * Tkinter 
  * Raspbery Pi -W
    * Micro SD Card
  * Etcher.io



### Tips:
* SSH login for Raspbery Pi
* shutdown: sudo shutdown -h now
* to exit python type: exit()
* Setup at: http://desertbot.io/setup-pi-zero-w-headless-wifi/


### Step 1: 

ssh-keygen -R raspberrypi.local
ssh pi@ramzipi.local

pass: enter your pass


setup at: https://www.raspberrypi.org/forums/viewtopic.php?f=91&t=35152


### Step 2: Create a directory of files for python

$mkdir python (or whatever you want to name it)



### Step 3: 
From Mac in a separate terminal send files: 

scp /Users/Ramzi/Documents/stockticker.py pi@ramzipi:python/
scp /Users/Ramzi/Documents/stockticker2.py pi@ramzipi:python/


### Step 4: How to Run python pile within raspberry pi:

python filename.py 


### Step 5: install quandl 


you'll need to follow it in this order otherwise it won't work, installing quandl will probably work fine in OSX but there is some dependencies not included on Raspbian 

1. pip install numpy
2. pip install pandas
3. sudo apt-get install libssl-dev
4. sudo apt-get install build-essential libssl-dev libffi-dev python-dev
5. pip install cryptography
6. pip install quandl


### Future Improvements:
1.  Auto Run Python file as raspberry pi connects to the internet
2. Show Opening and closing prices as time changes throughout the day
3. Better parse the data frame to only display prices and tickers more fluidly




## Check out the Video of how it works!!
<a href="http://www.youtube.com/watch?feature=player_embedded&v=bJVFLXuJrB4
" target="_blank"><img src="http://img.youtube.com/vi/bJVFLXuJrB4/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

