# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
# GH 12064
result = Timestamp(arg)
expected = Timestamp(datetime(2013, 1, 1), tz=pytz.FixedOffset(540))
assert result == expected
