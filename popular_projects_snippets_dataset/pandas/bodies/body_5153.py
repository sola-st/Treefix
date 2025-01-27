# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#19365
td = Timedelta(days=2, hours=6)

result = divmod(td, 53 * 3600 * 1e9)
assert result[0] == Timedelta(1, unit="ns")
assert isinstance(result[1], Timedelta)
assert result[1] == Timedelta(hours=1)

assert result
result = divmod(td, np.nan)
assert result[0] is NaT
assert result[1] is NaT
