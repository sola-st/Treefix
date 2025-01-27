# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_quarter.py
expected = "<BusinessQuarterEnd: startingMonth=3>"
assert repr(BQuarterEnd()) == expected
expected = "<BusinessQuarterEnd: startingMonth=3>"
assert repr(BQuarterEnd(startingMonth=3)) == expected
expected = "<BusinessQuarterEnd: startingMonth=1>"
assert repr(BQuarterEnd(startingMonth=1)) == expected
