# Extracted from https://stackoverflow.com/questions/42950/how-to-get-the-last-day-of-the-month
import datetime as dt
from dateutil.relativedelta import relativedelta

thisDate = dt.datetime(2017, 11, 17)

last_day_of_the_month = dt.datetime(thisDate.year, (thisDate + relativedelta(months=1)).month, 1) - dt.timedelta(days=1)
print last_day_of_the_month

datetime.datetime(2017, 11, 30, 0, 0)

import datetime as dt
import calendar
from dateutil.relativedelta import relativedelta

someDates = [dt.datetime.today() - dt.timedelta(days=x) for x in range(0, 10000)]

start1 = dt.datetime.now()
for thisDate in someDates:
    lastDay = dt.datetime(thisDate.year, (thisDate + relativedelta(months=1)).month, 1) - dt.timedelta(days=1)

print ('Time Spent= ', dt.datetime.now() - start1)


start2 = dt.datetime.now()
for thisDate in someDates:
    lastDay = dt.datetime(thisDate.year, 
                          thisDate.month, 
                          calendar.monthrange(thisDate.year, thisDate.month)[1])

print ('Time Spent= ', dt.datetime.now() - start2)

Time Spent=  0:00:00.097814
Time Spent=  0:00:00.109791

