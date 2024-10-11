# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
rng = date_range("1/1/2000", periods=20, tz=tzstr)

result = rng.take(range(5))
assert result.tz == rng.tz
assert result.freq == rng.freq
