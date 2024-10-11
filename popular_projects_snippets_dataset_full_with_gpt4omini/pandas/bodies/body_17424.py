# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_hour.py
assert _offset(-3).rollback(datetime(2014, 7, 5, 15, 0)) == datetime(
    2014, 7, 4, 17, 0
)
