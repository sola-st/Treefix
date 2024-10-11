# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_quarter.py
expected = "<QuarterBegin: startingMonth=3>"
assert repr(QuarterBegin()) == expected
expected = "<QuarterBegin: startingMonth=3>"
assert repr(QuarterBegin(startingMonth=3)) == expected
expected = "<QuarterBegin: startingMonth=1>"
assert repr(QuarterBegin(startingMonth=1)) == expected
