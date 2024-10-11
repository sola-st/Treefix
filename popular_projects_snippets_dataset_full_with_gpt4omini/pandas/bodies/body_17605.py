# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_quarter.py
assert QuarterBegin(startingMonth=1).is_anchored()
assert QuarterBegin().is_anchored()
assert not QuarterBegin(2, startingMonth=1).is_anchored()
