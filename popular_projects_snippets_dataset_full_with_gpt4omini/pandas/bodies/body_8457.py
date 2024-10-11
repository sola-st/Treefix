# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_misc.py
dti = DatetimeIndex(["2000-01-01", "2000-01-02", "2000-01-03"])

assert dti.is_month_start[0] == 1
