# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
values = DatetimeIndex([Timestamp("2020-01-01"), Timestamp("2020-01-02")])

result = values.get_indexer(target)
expected = np.array(positions, dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
