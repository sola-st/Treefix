# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
index = DatetimeIndex([pd.NaT, Timestamp("20130101"), Timestamp("20130102")])
result = index.take([-1, 0, 1])
expected = DatetimeIndex([index[-1], index[0], index[1]])
tm.assert_index_equal(result, expected)
