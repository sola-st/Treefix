# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_indexing.py
as_dense = np.array(as_dense)
arr = SparseArray(as_dense)

result = arr[slc]
expected = SparseArray(as_dense[slc])

tm.assert_sp_array_equal(result, expected)
