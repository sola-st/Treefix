# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
# Test properties on Periods with hourly frequency.
h_date1 = Period(freq="H", year=2007, month=1, day=1, hour=0)
h_date2 = Period(freq="2H", year=2007, month=1, day=1, hour=0)

for h_date in [h_date1, h_date2]:
    assert h_date.year == 2007
    assert h_date.quarter == 1
    assert h_date.month == 1
    assert h_date.day == 1
    assert h_date.weekday == 0
    assert h_date.dayofyear == 1
    assert h_date.hour == 0
    assert h_date.days_in_month == 31
    assert (
        Period(freq="H", year=2012, month=2, day=1, hour=0).days_in_month == 29
    )
