# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_scalar_compat.py
dt = DatetimeIndex(list(test_input))
func = getattr(dt, rounder)
result = func(freq)
expected = DatetimeIndex(list(expected))
assert expected.equals(result)
