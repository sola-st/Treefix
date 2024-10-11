# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_searchsorted.py
# GH8490
ser = Series([3, 1, 2])
res = ser.searchsorted([0, 3], sorter=np.argsort(ser))
exp = np.array([0, 2], dtype=np.intp)
tm.assert_numpy_array_equal(res, exp)
