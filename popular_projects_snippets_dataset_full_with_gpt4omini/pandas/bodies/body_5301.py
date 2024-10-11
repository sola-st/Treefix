# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
# Test properties on Periods with daily frequency.
b_date = Period(freq="B", year=2007, month=1, day=1)
#
assert b_date.year == 2007
assert b_date.quarter == 1
assert b_date.month == 1
assert b_date.day == 1
assert b_date.weekday == 0
assert b_date.dayofyear == 1
assert b_date.days_in_month == 31
assert Period(freq="B", year=2012, month=2, day=1).days_in_month == 29

d_date = Period(freq="D", year=2007, month=1, day=1)

assert d_date.year == 2007
assert d_date.quarter == 1
assert d_date.month == 1
assert d_date.day == 1
assert d_date.weekday == 0
assert d_date.dayofyear == 1
assert d_date.days_in_month == 31
assert Period(freq="D", year=2012, month=2, day=1).days_in_month == 29
