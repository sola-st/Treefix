# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# GH 35297

expected = DatetimeIndex(
    ["2020-11-01 01:00:00", "2020-11-02 01:00:00"],
    dtype="datetime64[ns, America/New_York]",
    freq="D",
    ambiguous=False,
)

# ambiguous keyword in start
timezone = "America/New_York"
start = Timestamp(year=2020, month=11, day=1, hour=1).tz_localize(
    timezone, ambiguous=False
)
result = date_range(start=start, periods=2, ambiguous=False)
tm.assert_index_equal(result, expected)

# ambiguous keyword in end
timezone = "America/New_York"
end = Timestamp(year=2020, month=11, day=2, hour=1).tz_localize(
    timezone, ambiguous=False
)
result = date_range(end=end, periods=2, ambiguous=False)
tm.assert_index_equal(result, expected)
