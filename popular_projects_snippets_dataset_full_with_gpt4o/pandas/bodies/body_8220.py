# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
# GH 21671
rng = DatetimeIndex([Timestamp("2011-01-01"), pd.NaT])
rng2 = DatetimeIndex(["2012-01-01", "2012-01-02"], tz="Asia/Tokyo")
result = rng.union(rng2)
expected = Index(
    [
        Timestamp("2011-01-01"),
        pd.NaT,
        Timestamp("2012-01-01", tz="Asia/Tokyo"),
        Timestamp("2012-01-02", tz="Asia/Tokyo"),
    ],
    dtype=object,
)
tm.assert_index_equal(result, expected)
