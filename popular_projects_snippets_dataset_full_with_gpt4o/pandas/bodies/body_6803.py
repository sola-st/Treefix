# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_indexing.py
ii = IntervalIndex.from_breaks(date_range("2018-01-01", periods=4))
result = ii.get_indexer(DatetimeIndex(["2018-01-02"]))
expected = np.array([0], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)

result = ii.get_indexer(DatetimeIndex(["2018-01-02"]).astype(str))
tm.assert_numpy_array_equal(result, expected)

# TODO this should probably be deprecated?
# https://github.com/pandas-dev/pandas/issues/47772
result = ii.get_indexer(DatetimeIndex(["2018-01-02"]).asi8)
tm.assert_numpy_array_equal(result, expected)
