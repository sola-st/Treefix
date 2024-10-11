# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
stamp = Timestamp("3/11/2012 05:00", tz=tzstr)
assert stamp.hour == 5

rng = date_range("3/11/2012 04:00", periods=10, freq="H", tz=tzstr)

assert stamp == rng[1]
