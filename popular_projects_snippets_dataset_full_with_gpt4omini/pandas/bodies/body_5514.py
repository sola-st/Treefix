# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_arithmetic.py
t1 = datetime(2013, 1, 1, tzinfo=timezone(timedelta(hours=-5)))
t2 = Timestamp("20130101").tz_localize("CET")

result = t1 - t2

assert isinstance(result, Timedelta)
assert result == Timedelta("0 days 06:00:00")

result = t2 - t1
assert isinstance(result, Timedelta)
assert result == Timedelta("-1 days +18:00:00")
