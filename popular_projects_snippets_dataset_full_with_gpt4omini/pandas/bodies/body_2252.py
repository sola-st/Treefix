# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH#45319
s = Series(
    [datetime.fromisoformat("1446-04-12 00:00:00+00:00")]
    + ([datetime.fromisoformat("1991-10-20 00:00:00+00:00")] * series_length)
)
result1 = to_datetime(s, errors="coerce", utc=True)

expected1 = Series(
    [NaT] + ([Timestamp("1991-10-20 00:00:00+00:00")] * series_length)
)

tm.assert_series_equal(result1, expected1)

result2 = to_datetime(s, errors="ignore", utc=True)

expected2 = Series(
    [datetime.fromisoformat("1446-04-12 00:00:00+00:00")]
    + ([datetime.fromisoformat("1991-10-20 00:00:00+00:00")] * series_length)
)

tm.assert_series_equal(result2, expected2)

with pytest.raises(OutOfBoundsDatetime, match="Out of bounds nanosecond timestamp"):
    to_datetime(s, errors="raise", utc=True)
