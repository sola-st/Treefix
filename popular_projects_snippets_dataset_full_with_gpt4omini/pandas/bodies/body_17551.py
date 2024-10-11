# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_quarter.py
assert BQuarterEnd(startingMonth=1).is_anchored()
assert BQuarterEnd().is_anchored()
assert not BQuarterEnd(2, startingMonth=1).is_anchored()
