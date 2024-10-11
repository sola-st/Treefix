# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_week.py
assert repr(Week(weekday=0)) == "<Week: weekday=0>"
assert repr(Week(n=-1, weekday=0)) == "<-1 * Week: weekday=0>"
assert repr(Week(n=-2, weekday=0)) == "<-2 * Weeks: weekday=0>"
