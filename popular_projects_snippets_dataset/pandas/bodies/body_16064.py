# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_searchsorted.py
ser = Series([1, 2, 90, 1000, 3e9])
res = ser.searchsorted([91, 2e6])
exp = np.array([3, 4], dtype=np.intp)
tm.assert_numpy_array_equal(res, exp)
