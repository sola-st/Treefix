# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_liboffsets.py
assert dt.weekday() == exp_week_day
assert get_firstbday(dt.year, dt.month) == exp_first_day
