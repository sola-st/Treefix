# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_setops.py
index = IntervalIndex.from_arrays([1, 0, 3, 2], [1, 2, 3, 4], closed=closed)
result = index.difference(index[:1], sort=sort)
expected = index[1:]
if sort is None:
    expected = expected.sort_values()
tm.assert_index_equal(result, expected)

# GH 19101: empty result, same dtype
result = index.difference(index, sort=sort)
expected = empty_index(dtype="int64", closed=closed)
tm.assert_index_equal(result, expected)

# GH 19101: empty result, different dtypes
other = IntervalIndex.from_arrays(
    index.left.astype("float64"), index.right, closed=closed
)
result = index.difference(other, sort=sort)
tm.assert_index_equal(result, expected)
