# Extracted from https://stackoverflow.com/questions/4530069/how-do-i-get-a-value-of-datetime-today-in-python-that-is-timezone-aware
import datetime
import pytz

pytz.utc.localize( datetime.datetime.utcnow() )  

pipenv install pytz

