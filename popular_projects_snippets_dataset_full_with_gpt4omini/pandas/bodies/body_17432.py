# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_hour.py
# GH 16867
bhour_us = CustomBusinessHour(calendar=USFederalHolidayCalendar())
t0 = datetime(2014, 1, 17, 15)
result = t0 + bhour_us * 8
expected = Timestamp("2014-01-21 15:00:00")
assert result == expected
