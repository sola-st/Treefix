# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#19365
td = Timedelta(hours=37)

# Numeric Others
result = td % 2
assert isinstance(result, Timedelta)
assert result == Timedelta(0)

result = td % 1e12
assert isinstance(result, Timedelta)
assert result == Timedelta(minutes=3, seconds=20)

result = td % int(1e12)
assert isinstance(result, Timedelta)
assert result == Timedelta(minutes=3, seconds=20)
