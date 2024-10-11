# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_common.py
assert date - offset2 == (-offset2)._apply(date)
