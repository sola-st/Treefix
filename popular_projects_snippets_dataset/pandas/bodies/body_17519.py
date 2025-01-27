# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_month.py
dt = datetime(2007, 1, 1)
offset = MonthEnd()

result = dt + offset
assert result == Timestamp(2007, 1, 31)

result = result + offset
assert result == Timestamp(2007, 2, 28)
