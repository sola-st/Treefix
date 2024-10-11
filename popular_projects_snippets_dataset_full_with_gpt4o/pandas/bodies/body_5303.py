# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
# Test properties on Periods with minutely frequency.
t_date = Period(freq="Min", year=2007, month=1, day=1, hour=0, minute=0)
#
assert t_date.quarter == 1
assert t_date.month == 1
assert t_date.day == 1
assert t_date.weekday == 0
assert t_date.dayofyear == 1
assert t_date.hour == 0
assert t_date.minute == 0
assert t_date.days_in_month == 31
assert (
    Period(freq="D", year=2012, month=2, day=1, hour=0, minute=0).days_in_month
    == 29
)
