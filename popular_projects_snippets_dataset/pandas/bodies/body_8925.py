# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_arithmetics.py
arr = SparseArray([0, 1], fill_value=0)
result = op(arr, [0, 1])
expected = op(arr, SparseArray([0, 1]))
tm.assert_sp_array_equal(result, expected)
