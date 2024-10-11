# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_arithmetic.py
t1 = Timestamp("2020-10-22T22:00:00+00:00")
t2 = datetime(2020, 10, 22, 22, tzinfo=timezone.utc)

result = t1 - t2

assert isinstance(result, Timedelta)
assert result == Timedelta("0 days")
