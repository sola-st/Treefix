# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
# https://github.com/pandas-dev/pandas/issues/31501
ser = Series(
    [0, 1, 2],
    DatetimeIndex(["2019-01-01", "2019-01-01T06:00:00", "2019-01-02"]),
)
result = ser[slc]
expected = ser.take(positions)
tm.assert_series_equal(result, expected)
