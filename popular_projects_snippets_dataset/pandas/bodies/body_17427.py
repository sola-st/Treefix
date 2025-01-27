# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_hour.py
offset = BusinessHour()

dt = datetime(2014, 7, 6, 15, 0)

result = offset.rollback(dt)
assert result == datetime(2014, 7, 4, 17)

result = offset.rollforward(dt)
assert result == datetime(2014, 7, 7, 9)
