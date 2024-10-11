# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
td = Timedelta(10, unit="d")
result = op(td, timedelta(days=9))
assert isinstance(result, Timedelta)
assert result == Timedelta(days=19)
