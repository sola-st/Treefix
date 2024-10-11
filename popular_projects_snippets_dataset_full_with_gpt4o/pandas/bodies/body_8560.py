# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
arr = [Timestamp("2011-01-01"), pd.NaT, Timestamp("2011-01-03")]
tm.assert_index_equal(Index(arr), DatetimeIndex(arr))
tm.assert_index_equal(Index(np.array(arr)), DatetimeIndex(np.array(arr)))

arr = [np.nan, pd.NaT, Timestamp("2011-01-03")]
tm.assert_index_equal(Index(arr), DatetimeIndex(arr))
tm.assert_index_equal(Index(np.array(arr)), DatetimeIndex(np.array(arr)))
