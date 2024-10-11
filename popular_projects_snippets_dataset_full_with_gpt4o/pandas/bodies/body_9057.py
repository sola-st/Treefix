# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_constructors.py
result = SparseArray([1, 2, 3], dtype="int")
expected = SparseArray([1, 2, 3], dtype=int)
tm.assert_sp_array_equal(result, expected)
