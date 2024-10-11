# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_indexing.py
data = np.array([1, np.nan, 0, 3, 0])
sparse = SparseArray(data, fill_value=0)

exp = SparseArray(np.take(data, [0]), fill_value=0)
tm.assert_sp_array_equal(sparse.take([0]), exp)

exp = SparseArray(np.take(data, [1, 3, 4]), fill_value=0)
tm.assert_sp_array_equal(sparse.take([1, 3, 4]), exp)
