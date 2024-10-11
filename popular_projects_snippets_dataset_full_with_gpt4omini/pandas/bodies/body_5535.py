# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
# GH#31929
ts = Timestamp(2020, 12, 31, tzinfo=timezone.utc)
expected = Timestamp("2020-12-31", tzinfo=timezone.utc)
assert ts == expected
