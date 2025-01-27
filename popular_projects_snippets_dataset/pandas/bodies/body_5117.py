# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
td = Timedelta("1 day")
other = np.array(2)
assert other.ndim == 0
expected = Timedelta("2 days")

res = td * other
assert type(res) is Timedelta
assert res == expected

res = other * td
assert type(res) is Timedelta
assert res == expected
