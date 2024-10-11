# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
# GH 34621

assert Period(day + hour + sec_float).start_time.nanosecond == expected
