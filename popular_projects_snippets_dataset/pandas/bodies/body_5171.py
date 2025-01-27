# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
class Other:
    pass

other = Other()

td = Timedelta("1 day")
assert td.__add__(other) is NotImplemented
assert td.__sub__(other) is NotImplemented
assert td.__truediv__(other) is NotImplemented
assert td.__mul__(other) is NotImplemented
assert td.__floordiv__(other) is NotImplemented
