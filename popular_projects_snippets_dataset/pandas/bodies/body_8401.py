# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# GH 12064
result = date_range(
    "2013-01-01 00:00:00+09:00", "2013/01/01 02:00:00+09:00", freq="H"
)
expected = DatetimeIndex(
    [
        Timestamp("2013-01-01 00:00:00+09:00"),
        Timestamp("2013-01-01 01:00:00+09:00"),
        Timestamp("2013-01-01 02:00:00+09:00"),
    ],
    freq="H",
)
tm.assert_index_equal(result, expected)
