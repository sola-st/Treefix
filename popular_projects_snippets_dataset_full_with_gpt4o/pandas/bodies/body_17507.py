# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_week.py
assert (
    repr(LastWeekOfMonth(n=2, weekday=1)) == "<2 * LastWeekOfMonths: weekday=1>"
)
