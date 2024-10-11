# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_day.py
dt = date(2012, 9, 15)

result = offset.rollback(dt)
assert result == datetime(2012, 9, 14)

result = offset.rollforward(dt)
assert result == datetime(2012, 9, 17)

offset = offsets.Day()
result = offset.rollback(dt)
assert result == datetime(2012, 9, 15)

result = offset.rollforward(dt)
assert result == datetime(2012, 9, 15)
