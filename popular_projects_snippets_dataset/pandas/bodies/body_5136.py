# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#18846
td = Timedelta(hours=3, minutes=3)
scalar = Timedelta(hours=3, minutes=4)

# scalar others
# x // Timedelta is defined only for timedelta-like x. int-like,
# float-like, and date-like, in particular, should all either
# a) raise TypeError directly or
# b) return NotImplemented, following which the reversed
#    operation will raise TypeError.
assert td.__rfloordiv__(scalar) == 1
assert (-td).__rfloordiv__(scalar.to_pytimedelta()) == -2
assert (2 * td).__rfloordiv__(scalar.to_timedelta64()) == 0
