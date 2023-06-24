# from pytz import timezone
# from datetime import datetime
# today = datetime.now(timezone('Asia/Seoul'))
# print(today)

from pytz import timezone
from datetime import datetime
import time, win32con, win32api, win32gui
import schedule

now = datetime.now(timezone('Asia/Seoul'))

day_of_week = now.weekday() #Date Of Week 현재 요일
year = now.year
month = now.month
day = now.day
hour = now.hour
min = now.minute

print(day_of_week,year,month,day,hour,min)