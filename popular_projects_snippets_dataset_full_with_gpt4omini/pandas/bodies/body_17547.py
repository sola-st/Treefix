# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_quarter.py
assert BQuarterBegin(startingMonth=1).is_anchored()
assert BQuarterBegin().is_anchored()
assert not BQuarterBegin(2, startingMonth=1).is_anchored()
