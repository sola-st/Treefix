# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_common.py
# root cause of GH#456: __ne__ was not implemented
offset1 = _offset()
offset2 = _offset()
assert not offset1 != offset2
assert offset1 == offset2
