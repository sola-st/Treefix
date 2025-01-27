# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_arithmetics.py
result = ufunc(arr)
fill_value = ufunc(arr.fill_value)
expected = SparseArray(ufunc(np.asarray(arr)), fill_value=fill_value)
tm.assert_sp_array_equal(result, expected)
