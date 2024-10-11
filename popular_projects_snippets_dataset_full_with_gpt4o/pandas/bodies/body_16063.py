# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_searchsorted.py
ser = Series([1, 2, 90, 1000, 3e9])
res = ser.searchsorted(30)
assert is_scalar(res)
assert res == 2

res = ser.searchsorted([30])
exp = np.array([2], dtype=np.intp)
tm.assert_numpy_array_equal(res, exp)
