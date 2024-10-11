# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
offset = _create_offset(offset_types)
assert offset.n == 1

neg_offset = offset * -1
assert neg_offset.n == -1

mul_offset = offset * 3
assert mul_offset.n == 3
