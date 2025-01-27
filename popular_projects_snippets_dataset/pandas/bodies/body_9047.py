# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_indexing.py
exp = SparseArray(np.take(arr_data, [2, 3]))
tm.assert_sp_array_equal(arr.take([2, 3]), exp)

exp = SparseArray(np.take(arr_data, [0, 1, 2]))
tm.assert_sp_array_equal(arr.take([0, 1, 2]), exp)
