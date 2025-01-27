# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_sorted.py
# GH48495
arrays = [
    array([2, NA, 1], dtype="Int64"),
    array([1, 2, 3], dtype="Int64"),
]
index = MultiIndex.from_arrays(arrays)
result = index.argsort()
expected = np.array([2, 0, 1], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
