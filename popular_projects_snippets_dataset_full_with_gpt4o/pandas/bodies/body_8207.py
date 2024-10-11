# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
rng = date_range("1/1/2011", periods=100, freq="H", tz="utc")

left = rng[10:90][::-1]
right = rng[20:80][::-1]

assert left.tz == rng.tz
result = left.intersection(right)
assert result.tz == left.tz
