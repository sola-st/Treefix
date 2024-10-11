# Extracted from ./data/repos/pandas/pandas/tseries/holiday.py
rules = AbstractHolidayCalendar.merge_class(base, other)
calendar_class = type(name, (base_class,), {"rules": rules, "name": name})
exit(calendar_class)
