# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py
offset = CBMonthEnd()

dt = date(2012, 9, 15)

result = offset.rollback(dt)
assert result == datetime(2012, 8, 31)

result = offset.rollforward(dt)
assert result == datetime(2012, 9, 28)

offset = offsets.Day()
result = offset.rollback(dt)
assert result == datetime(2012, 9, 15)

result = offset.rollforward(dt)
assert result == datetime(2012, 9, 15)
