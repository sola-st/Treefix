# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_unary.py
arr = np.array([0, 1, np.nan, 2])
sparray = SparseArray(arr, fill_value=fill_value)
result = op(sparray)
expected = SparseArray(op(arr), fill_value=op(fill_value))
tm.assert_sp_array_equal(result, expected)
