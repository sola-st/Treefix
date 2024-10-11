# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_array.py
# https://github.com/pandas-dev/pandas/issues/26946
sparse = SparseArray([fill_value] * 10 + [1.1, 2.2], fill_value=fill_value)
r1, r2 = np.modf(sparse)
e1, e2 = np.modf(np.asarray(sparse))
tm.assert_sp_array_equal(r1, SparseArray(e1, fill_value=fill_value))
tm.assert_sp_array_equal(r2, SparseArray(e2, fill_value=fill_value))
