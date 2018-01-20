# headlesspi


SSH login for Raspbery Pi
shutdown: sudo shutdown -h now

to exit python type: exit()

Setup at: http://desertbot.io/setup-pi-zero-w-headless-wifi/


Step 1: 

ssh-keygen -R raspberrypi.local
ssh pi@ramzipi.local

pass: enter youur pass


setup at: https://www.raspberrypi.org/forums/viewtopic.php?f=91&t=35152


Step 2: Create a directory of files for python

$mkdir python (or whatever you want to name it)



Step 3: 
From Mac in a sepearte terminal send files: 

scp /Users/Ramzi/Documents/robotmouth.py pi@ramzipi:python/
scp /Users/Ramzi/Documents/mouth.bmp pi@ramzipi:python/
scp /Users/Ramzi/Documents/protraitclock.py pi@ramzipi:python/
scp /Users/Ramzi/Documents/cpu.py pi@ramzipi:python/
