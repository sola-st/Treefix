# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_liboffsets.py
ts = Timestamp("1929-05-05")
assert liboffsets.shift_month(ts, months, day_opt=day_opt) == expected
