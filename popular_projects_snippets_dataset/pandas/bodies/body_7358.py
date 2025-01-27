# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_constructors.py
arr = [Timedelta("1 days"), pd.NaT, Timedelta("3 days")]
tm.assert_index_equal(pd.Index(arr), TimedeltaIndex(arr))
tm.assert_index_equal(pd.Index(np.array(arr)), TimedeltaIndex(np.array(arr)))

arr = [np.nan, pd.NaT, Timedelta("1 days")]
tm.assert_index_equal(pd.Index(arr), TimedeltaIndex(arr))
tm.assert_index_equal(pd.Index(np.array(arr)), TimedeltaIndex(np.array(arr)))
