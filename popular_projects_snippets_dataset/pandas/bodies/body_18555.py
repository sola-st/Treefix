# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_liboffsets.py
dt = datetime(2017, 11, 30)
assert liboffsets.shift_month(dt, months, day_opt=day_opt) == expected
