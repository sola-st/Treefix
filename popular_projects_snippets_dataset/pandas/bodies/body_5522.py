# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_arithmetic.py
# GH 32619
dt = datetime(2021, 1, 1)
ts1 = Timestamp(dt, tz=utc_fixture)
ts2 = Timestamp(dt, tz=utc_fixture2)
result = ts1 - ts2
expected = Timedelta(0)
assert result == expected
