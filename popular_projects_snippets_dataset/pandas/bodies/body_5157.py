# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#19365
result = divmod(timedelta(days=2, hours=6), Timedelta(days=1))
assert result[0] == 2
assert isinstance(result[1], Timedelta)
assert result[1] == Timedelta(hours=6)
