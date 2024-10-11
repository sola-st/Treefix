# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_unary_ops.py
tz = tz_aware_fixture
# GH#14621, GH#7825
# replacing datetime components with and w/o presence of a timezone
# test all
ts = Timestamp("2016-01-01 09:00:00.000000123", tz=tz)
result = ts.replace(
    year=2015,
    month=2,
    day=2,
    hour=0,
    minute=5,
    second=5,
    microsecond=5,
    nanosecond=5,
)
expected = Timestamp("2015-02-02 00:05:05.000005005", tz=tz)
assert result == expected
