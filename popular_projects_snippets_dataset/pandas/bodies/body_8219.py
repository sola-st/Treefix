# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
# non-overlapping
# GH#39328 as of 2.0 we cast these to UTC instead of object
rng = date_range("2012-11-15 00:00:00", periods=6, freq="H", tz="US/Central")

rng2 = date_range("2012-11-15 12:00:00", periods=6, freq="H", tz="US/Eastern")

result = getattr(rng, setop)(rng2)

left = rng.tz_convert("UTC")
right = rng2.tz_convert("UTC")
expected = getattr(left, setop)(right)
tm.assert_index_equal(result, expected)
assert result.tz == left.tz
if len(result):
    assert result[0].tz is timezone.utc
    assert result[-1].tz is timezone.utc
