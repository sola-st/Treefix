# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#19365
td = Timedelta(days=2, hours=6)

result = divmod(td, offsets.Hour(-4))
assert result[0] == -14
assert isinstance(result[1], Timedelta)
assert result[1] == Timedelta(hours=-2)
