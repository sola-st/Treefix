# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_arithmetic.py
t1 = Timestamp("20130101").tz_localize("US/Eastern")
t2 = Timestamp("20130101").tz_localize("CET")

result = t1 - t2

assert isinstance(result, Timedelta)
assert result == Timedelta("0 days 06:00:00")
