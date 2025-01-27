# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_liboffsets.py
month = 6
day_opt = "end"  # `other` will be compared to June 30.

assert roll_qtrday(other, n, month, day_opt, modby=12) == expected[n]
