# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py
assert CDay(10).rollback(datetime(2007, 12, 31)) == datetime(2007, 12, 31)
