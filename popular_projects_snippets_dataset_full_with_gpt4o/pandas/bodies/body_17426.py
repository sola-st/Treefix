# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_hour.py
assert _offset(-3).rollforward(datetime(2014, 7, 5, 16, 0)) == datetime(
    2014, 7, 7, 9
)
