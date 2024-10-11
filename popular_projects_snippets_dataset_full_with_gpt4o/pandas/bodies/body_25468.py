# Extracted from ./data/repos/pandas/pandas/tseries/holiday.py
try:
    name = cls.name
except AttributeError:
    name = cls.__name__
holiday_calendars[name] = cls
