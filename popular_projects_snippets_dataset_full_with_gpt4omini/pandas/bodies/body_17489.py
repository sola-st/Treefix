# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
# GH 45890, 45643
offset = DateOffset(n)
assert offset._offset == timedelta(1)
result = Timestamp(2022, 1, 2) + offset
expected = Timestamp(2022, 1, 2 + n)
assert result == expected
