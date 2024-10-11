# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_astype.py
vals = np.array([1, 2, 3])
arr = SparseArray(vals, fill_value=1)
typ = np.dtype(any_real_numpy_dtype)
res = arr.astype(typ)
tm.assert_numpy_array_equal(res, vals.astype(any_real_numpy_dtype))
