from datetime import datetime
import time, win32con, win32api, win32gui
import schedule

now = datetime.now()

DOW = now.weekday() #Date Of Week 현재 요일
year = now.year
month = now.month
day = now.day
hour = now.hour
min = now.minute

print(DOW,year,month,day,hour,min)