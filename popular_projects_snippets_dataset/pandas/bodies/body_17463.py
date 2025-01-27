# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
assert DateOffset(**{arithmatic_offset_type: 1}) * n + dt == Timestamp(expected)
assert n * DateOffset(**{arithmatic_offset_type: 1}) + dt == Timestamp(expected)
assert dt + DateOffset(**{arithmatic_offset_type: 1}) * n == Timestamp(expected)
assert dt + n * DateOffset(**{arithmatic_offset_type: 1}) == Timestamp(expected)
