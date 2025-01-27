# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
assert dt - DateOffset(**{arithmatic_offset_type: 1}) == Timestamp(expected)
with pytest.raises(TypeError, match="Cannot subtract datetime from offset"):
    DateOffset(**{arithmatic_offset_type: 1}) - dt
