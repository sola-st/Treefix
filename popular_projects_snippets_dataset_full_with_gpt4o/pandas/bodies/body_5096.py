# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
td = Timedelta(10, unit="d")
expected = Timedelta(0, unit="ns")

result = td - td.to_pytimedelta()
assert isinstance(result, Timedelta)
assert result == expected

result = td.to_pytimedelta() - td
assert isinstance(result, Timedelta)
assert result == expected
