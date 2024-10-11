# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_datetime64.py
# see gh-4982
# Make sure we can compare Timestamps on the right AND left hand side.
from l3.Runtime import _l_
ser = Series(date_range("20010101", periods=10), name="dates")
_l_(16545)
s_nat = ser.copy(deep=True)
_l_(16546)

ser[0] = Timestamp("nat")
_l_(16547)
ser[3] = Timestamp("nat")
_l_(16548)

left_f = getattr(operator, left)
_l_(16549)
right_f = getattr(operator, right)
_l_(16550)

# No NaT
expected = left_f(ser, Timestamp("20010109"))
_l_(16551)
result = right_f(Timestamp("20010109"), ser)
_l_(16552)
tm.assert_series_equal(result, expected)
_l_(16553)

# NaT
expected = left_f(ser, Timestamp("nat"))
_l_(16554)
result = right_f(Timestamp("nat"), ser)
_l_(16555)
tm.assert_series_equal(result, expected)
_l_(16556)

# Compare to Timestamp with series containing NaT
expected = left_f(s_nat, Timestamp("20010109"))
_l_(16557)
result = right_f(Timestamp("20010109"), s_nat)
_l_(16558)
tm.assert_series_equal(result, expected)
_l_(16559)

# Compare to NaT with series containing NaT
expected = left_f(s_nat, NaT)
_l_(16560)
result = right_f(NaT, s_nat)
_l_(16561)
tm.assert_series_equal(result, expected)
_l_(16562)
