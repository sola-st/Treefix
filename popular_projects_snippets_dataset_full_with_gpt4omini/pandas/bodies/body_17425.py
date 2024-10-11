# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_hour.py
assert offset1.rollforward(dt) == dt
assert offset2.rollforward(dt) == dt

d = datetime(2014, 7, 1, 0)
assert offset1.rollforward(d) == datetime(2014, 7, 1, 9)
assert offset2.rollforward(d) == datetime(2014, 7, 1, 9)
