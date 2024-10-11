# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_quarter.py
assert QuarterEnd(startingMonth=1).is_anchored()
assert QuarterEnd().is_anchored()
assert not QuarterEnd(2, startingMonth=1).is_anchored()
