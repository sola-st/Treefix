# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
td = Timedelta(10, unit="d")
result = op(td, np.timedelta64(-4, "D"))
assert isinstance(result, Timedelta)
assert result == Timedelta(days=6)
