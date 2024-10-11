# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
# GH 18898
# As of 2.0 (GH 49416), nanosecond should not be accepted positionally
expected = Timestamp(datetime(2000, 1, 2, 3, 4, 5, 6), tz=result.tz)
expected = expected + Timedelta(nanoseconds=1)
assert result == expected
