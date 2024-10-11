# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
rng = DatetimeIndex(["1-1-2000 00:00:01"])
assert rng[0].second == 1
