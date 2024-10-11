# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py
assert CBMonthBegin(10).rollback(dt) == datetime(2008, 1, 1)
