# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#33146
obj = frame_or_series(
    [1] * 5,
    index=DatetimeIndex(
        [
            Timestamp("2019-12-30"),
            Timestamp("2020-01-01"),
            Timestamp("2019-12-25"),
            Timestamp("2020-01-02 23:59:59.999999999"),
            Timestamp("2019-12-19"),
        ],
        tz=tz_aware_fixture,
    ),
)
expected = frame_or_series(
    [1] * 2,
    index=DatetimeIndex(
        [
            Timestamp("2020-01-01"),
            Timestamp("2020-01-02 23:59:59.999999999"),
        ],
        tz=tz_aware_fixture,
    ),
)
indexer = slice("2020-01-01", indexer_end)

result = obj[indexer]
tm.assert_equal(result, expected)

result = obj.loc[indexer]
tm.assert_equal(result, expected)
