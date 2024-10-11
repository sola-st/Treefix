# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
td = Timedelta(10, unit="d")
expected = Timedelta(0, unit="ns")

result = td - td.to_timedelta64()
assert isinstance(result, Timedelta)
assert result == expected

result = td.to_timedelta64() - td
assert isinstance(result, Timedelta)
assert result == expected
