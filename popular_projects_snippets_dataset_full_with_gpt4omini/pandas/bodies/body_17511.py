# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_month.py
dt, expected = case
assert_is_on_offset(SemiMonthEnd(), dt, expected)
