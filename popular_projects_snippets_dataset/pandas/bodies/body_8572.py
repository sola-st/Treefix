# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# GH 18595
start = Timestamp("2013-01-01 06:00:00", tz="America/Los_Angeles")
end = Timestamp("2013-01-02 06:00:00", tz="America/Los_Angeles")
result = date_range(freq="D", start=start, end=end, tz=tz)
expected = DatetimeIndex(
    ["2013-01-01 06:00:00", "2013-01-02 06:00:00"],
    tz="America/Los_Angeles",
    freq="D",
)
tm.assert_index_equal(result, expected)
# Especially assert that the timezone is consistent for pytz
assert pytz.timezone("America/Los_Angeles") is result.tz
