# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_array.py
vals = np.array(vals)
arr = SparseArray(vals, fill_value=fill_value)

res = arr.to_dense()
tm.assert_numpy_array_equal(res, vals)
