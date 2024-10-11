# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
# Test properties on Periods with daily frequency.
w_date = Period(freq="W", year=2007, month=1, day=7)
assert w_date.year == 2007
assert w_date.quarter == 1
assert w_date.month == 1
assert w_date.week == 1
assert (w_date - 1).week == 52
assert w_date.days_in_month == 31

exp = Period(freq="W", year=2012, month=2, day=1)
assert exp.days_in_month == 29

msg = INVALID_FREQ_ERR_MSG
with pytest.raises(ValueError, match=msg):
    Period(freq="WK", year=2007, month=1, day=7)
