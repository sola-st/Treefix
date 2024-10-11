# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_datetime.py

# GH 12050
# indexing on a series with a datetimeindex with tz
index = date_range("2015-01-01", periods=2, tz="utc")

ser = Series(range(2), index=index, dtype="int64")

# list-like indexing

for sel in (index, list(index)):
    # getitem
    result = indexer_sl(ser)[sel]
    expected = ser.copy()
    if sel is not index:
        expected.index = expected.index._with_freq(None)
    tm.assert_series_equal(result, expected)

    # setitem
    result = ser.copy()
    indexer_sl(result)[sel] = 1
    expected = Series(1, index=index)
    tm.assert_series_equal(result, expected)

# single element indexing

# getitem
assert indexer_sl(ser)[index[1]] == 1

# setitem
result = ser.copy()
indexer_sl(result)[index[1]] = 5
expected = Series([0, 5], index=index)
tm.assert_series_equal(result, expected)
