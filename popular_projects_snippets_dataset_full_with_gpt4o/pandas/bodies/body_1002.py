# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_sorted.py
# GH48495
arrays = [
    array([2, NA, 1], dtype="Int64"),
    array([1, 2, 3], dtype="Int64"),
]
index = MultiIndex.from_arrays(arrays)
index = index.sort_values()
result = DataFrame(range(3), index=index)

arrays = [
    array([1, 2, NA], dtype="Int64"),
    array([3, 1, 2], dtype="Int64"),
]
index = MultiIndex.from_arrays(arrays)
expected = DataFrame(range(3), index=index)

tm.assert_frame_equal(result, expected)
