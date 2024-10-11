# Extracted from ./data/repos/pandas/pandas/tests/tslibs/test_period_asfreq.py
# 5000 is PeriodDtypeCode for BusinessDay
args = (2013, 10, day, 0, 0, 0, 0, 0, 5000)
assert period_ordinal(*args) == expected
