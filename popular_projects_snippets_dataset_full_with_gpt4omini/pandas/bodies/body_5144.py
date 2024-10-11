# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#19365
td = Timedelta(hours=37)

# Timedelta-like others
result = td % Timedelta(hours=6)
assert isinstance(result, Timedelta)
assert result == Timedelta(hours=1)

result = td % timedelta(minutes=60)
assert isinstance(result, Timedelta)
assert result == Timedelta(0)

result = td % NaT
assert result is NaT
