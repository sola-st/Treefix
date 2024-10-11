# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
offset = DateOffset(minutes=2, nanoseconds=9)
ts = Timestamp(4)
result = ts + offset
expected = Timestamp("1970-01-01 00:02:00.000000013")
assert result == expected
result -= offset
assert result == ts
result = offset + ts
assert result == expected
