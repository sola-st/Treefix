# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
assert not DateOffset(2).is_anchored()
assert DateOffset(1).is_anchored()
