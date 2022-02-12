import os
from datetime import datetime
from time import sleep

while True:
    try:
        wanted = (input("What time do you want to shut down the computer?(HH:MM)\n"))
        newlist = wanted.split(":")   
        y = int(newlist[1])
        x = int(newlist[0])
        break
    except IndexError:
        print(f"Please type correctly!(like 02:45 or 23:19)")
        sleep(1)


now = datetime.now()

if y < now.minute:
    hours = x - now.hour-1
    if hours < 0:
        hours += 24
elif y > now.minute:
    hours = x - now.hour 
    if hours < 0:
        hours += 24


minutes = y - now.minute
if minutes < 0:
    minutes += 60


seconds = (hours*60*60) + ((minutes-1)*60) + 60-now.second

while True:
    print(f"{seconds} seconds to shutdown!")
    seconds -= 1
    sleep(1)
    if seconds <= 0:
        os.system("shutdown /s /t 1")
        break
        
    

    
    