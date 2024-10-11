# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_liboffsets.py
assert dt.weekday() == exp_week_day
assert get_lastbday(dt.year, dt.month) == exp_last_day
