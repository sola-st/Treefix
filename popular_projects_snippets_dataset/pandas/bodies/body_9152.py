# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_dtypes.py
# GH 38316
index = IntervalIndex.from_breaks(np.arange(3, dtype="uint64"))

result = CategoricalIndex(index).dtype.categories
expected = IntervalIndex.from_arrays(
    [0, 1], [1, 2], dtype="interval[uint64, right]"
)
tm.assert_index_equal(result, expected)
