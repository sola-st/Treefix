# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py
assert CBMonthEnd(10).rollback(dt) == datetime(2007, 12, 31)
