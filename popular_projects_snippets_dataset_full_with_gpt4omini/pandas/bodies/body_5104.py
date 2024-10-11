# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
result = offsets.Hour(1) - Timedelta(10, unit="d")
assert isinstance(result, Timedelta)
assert result == Timedelta(-239, unit="h")
