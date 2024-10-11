# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
td = Timedelta("1 day")

other = np.array(1)
res = td / other
assert isinstance(res, Timedelta)
assert res == td
