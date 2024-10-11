# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_common.py
assert dt + 10 * offset1 == dt + offset_box(10)
assert dt + 5 * offset1 == dt + offset_box(5)
