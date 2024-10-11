# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#19365
td = Timedelta(hours=37)

result = td % offsets.Hour(5)
assert isinstance(result, Timedelta)
assert result == Timedelta(hours=2)
