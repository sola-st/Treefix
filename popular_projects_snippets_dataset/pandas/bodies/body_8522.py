# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
# https://github.com/pandas-dev/pandas/issues/33741
values = DatetimeIndex([Timestamp("2020-01-01"), Timestamp("2020-01-02")])
result = values.get_indexer(target)
expected = np.array([0, 1], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
