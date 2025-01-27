# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_indexing.py
arr = SparseArray([0, 1, 2])
result = arr[[True, False, True]]
expected = SparseArray([0, 2])
tm.assert_sp_array_equal(result, expected)
