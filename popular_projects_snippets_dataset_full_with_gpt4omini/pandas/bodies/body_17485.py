# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
offset = DateOffset(**offset_kwargs)
ts = Timestamp(0)
result = ts + offset
expected = Timestamp(expected_arg)
assert result == expected
result -= offset
assert result == ts
result = offset + ts
assert result == expected
