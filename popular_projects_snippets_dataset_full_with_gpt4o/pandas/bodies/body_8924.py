# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_arithmetics.py
s = SparseArray([True, True, False, False])
t = SparseArray([True, False, True, False])
result = s ^ t
sp_index = pd.core.arrays.sparse.IntIndex(4, np.array([0, 1, 2], dtype="int32"))
expected = SparseArray([False, True, True], sparse_index=sp_index)
tm.assert_sp_array_equal(result, expected)
