# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_day.py
calendar = USFederalHolidayCalendar()
dt = datetime(2014, 1, 17)
assert_offset_equal(CDay(calendar=calendar), dt, datetime(2014, 1, 21))
