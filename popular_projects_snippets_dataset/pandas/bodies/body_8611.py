# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_join.py
rng = date_range("1/1/2011", periods=100, freq="H", tz="utc")

left = rng.tz_convert("US/Eastern")
right = rng.tz_convert("Europe/Berlin")

result = left.join(left[:-5], how=join_type)
assert isinstance(result, DatetimeIndex)
assert result.tz == left.tz

result = left.join(right[:-5], how=join_type)
assert isinstance(result, DatetimeIndex)
assert result.tz is timezone.utc
