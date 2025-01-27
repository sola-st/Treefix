# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_combine_concat.py
other = "integer" if kind == "block" else "block"
a = SparseArray([1, 0, 0, 2], kind=kind)
b = SparseArray([1, 0, 2, 2], kind=other)

result = SparseArray._concat_same_type([a, b])
expected = np.array([1, 2, 1, 2, 2], dtype="int64")
tm.assert_numpy_array_equal(result.sp_values, expected)
assert result.kind == kind
