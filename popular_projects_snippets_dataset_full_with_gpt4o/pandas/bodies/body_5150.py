# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#19365
td = Timedelta(minutes=3)

result = timedelta(minutes=4) % td
assert isinstance(result, Timedelta)
assert result == Timedelta(minutes=1)
