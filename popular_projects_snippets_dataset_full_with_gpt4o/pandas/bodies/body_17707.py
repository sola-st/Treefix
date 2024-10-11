# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_day.py
assert _offset(10).rollforward(datetime(2008, 1, 5)) == datetime(2008, 1, 7)
