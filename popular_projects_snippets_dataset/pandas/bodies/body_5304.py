# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
# Test properties on Periods with secondly frequency.
s_date = Period(
    freq="Min", year=2007, month=1, day=1, hour=0, minute=0, second=0
)
#
assert s_date.year == 2007
assert s_date.quarter == 1
assert s_date.month == 1
assert s_date.day == 1
assert s_date.weekday == 0
assert s_date.dayofyear == 1
assert s_date.hour == 0
assert s_date.minute == 0
assert s_date.second == 0
assert s_date.days_in_month == 31
assert (
    Period(
        freq="Min", year=2012, month=2, day=1, hour=0, minute=0, second=0
    ).days_in_month
    == 29
)
