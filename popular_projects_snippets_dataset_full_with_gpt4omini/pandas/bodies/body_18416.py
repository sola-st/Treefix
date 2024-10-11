# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# see gh-4982
# Make sure we can compare Timestamps on the right AND left hand side.
from l3.Runtime import _l_
ser = Series(date_range("20010101", periods=10), name="dates")
_l_(4967)
s_nat = ser.copy(deep=True)
_l_(4968)

ser[0] = Timestamp("nat")
_l_(4969)
ser[3] = Timestamp("nat")
_l_(4970)

left_f = getattr(operator, left)
_l_(4971)
right_f = getattr(operator, right)
_l_(4972)

# No NaT
expected = left_f(ser, Timestamp("20010109"))
_l_(4973)
result = right_f(Timestamp("20010109"), ser)
_l_(4974)
tm.assert_series_equal(result, expected)
_l_(4975)

# NaT
expected = left_f(ser, Timestamp("nat"))
_l_(4976)
result = right_f(Timestamp("nat"), ser)
_l_(4977)
tm.assert_series_equal(result, expected)
_l_(4978)

# Compare to Timestamp with series containing NaT
expected = left_f(s_nat, Timestamp("20010109"))
_l_(4979)
result = right_f(Timestamp("20010109"), s_nat)
_l_(4980)
tm.assert_series_equal(result, expected)
_l_(4981)

# Compare to NaT with series containing NaT
expected = left_f(s_nat, NaT)
_l_(4982)
result = right_f(NaT, s_nat)
_l_(4983)
tm.assert_series_equal(result, expected)
_l_(4984)
