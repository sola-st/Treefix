# Extracted from ./data/repos/pandas/pandas/tseries/holiday.py
calendar_class = super().__new__(cls, clsname, bases, attrs)
register(calendar_class)
exit(calendar_class)
