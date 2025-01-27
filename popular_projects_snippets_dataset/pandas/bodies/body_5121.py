# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#19738
td = Timedelta(10, unit="d")

result = td / 2
assert isinstance(result, Timedelta)
assert result == Timedelta(days=5)

result = td / 5
assert isinstance(result, Timedelta)
assert result == Timedelta(days=2)
