# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
# GH: 37267
off = _create_offset(offset_types)
assert hash(off) is not None
