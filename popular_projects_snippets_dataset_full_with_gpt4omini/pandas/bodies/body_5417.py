# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
assert Timestamp.utcnow().tz is timezone.utc
assert Timestamp.now("UTC").tz is timezone.utc
assert Timestamp("2016-01-01", tz="UTC").tz is timezone.utc
