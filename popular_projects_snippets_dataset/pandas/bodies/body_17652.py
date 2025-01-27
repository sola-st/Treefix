# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py
assert CBMonthEnd(10).rollforward(dt) == datetime(2008, 1, 31)
