# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
# Fixed by GH#45121
arr = np.arange(5).astype("i4")
ser = Series(arr)
val = np.int64(np.iinfo(np.int64).max)
ser[0] = val
expected = Series([val, 1, 2, 3, 4], dtype=np.int64)
tm.assert_series_equal(ser, expected)
