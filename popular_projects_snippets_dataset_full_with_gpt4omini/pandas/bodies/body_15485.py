# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_setitem.py
arr = np.arange(5).astype("c8")
ser = Series(arr)
val = np.finfo(np.float64).max
val = val.astype("c16")

# GH#32878 used to coerce val to inf+0.000000e+00j
ser[0] = val
assert ser[0] == val
expected = Series([val, 1, 2, 3, 4], dtype="c16")
tm.assert_series_equal(ser, expected)
