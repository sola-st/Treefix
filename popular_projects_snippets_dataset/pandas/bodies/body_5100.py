# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
td = Timedelta(10, unit="d")
result = td - offsets.Hour(1)
assert isinstance(result, Timedelta)
assert result == Timedelta(239, unit="h")
