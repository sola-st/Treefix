# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_indexing.py
exp = SparseArray(np.take(arr_data, [-1]))
tm.assert_sp_array_equal(arr.take([-1]), exp)

exp = SparseArray(np.take(arr_data, [-4, -3, -2]))
tm.assert_sp_array_equal(arr.take([-4, -3, -2]), exp)
