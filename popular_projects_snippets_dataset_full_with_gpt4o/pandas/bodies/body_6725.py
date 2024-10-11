# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_setops.py
index = monotonic_index(0, 11, closed=closed)
result = index[1:].symmetric_difference(index[:-1], sort=sort)
expected = IntervalIndex([index[0], index[-1]])
if sort is None:
    tm.assert_index_equal(result, expected)
assert tm.equalContents(result, expected)

# GH 19101: empty result, same dtype
result = index.symmetric_difference(index, sort=sort)
expected = empty_index(dtype="int64", closed=closed)
if sort is None:
    tm.assert_index_equal(result, expected)
assert tm.equalContents(result, expected)

# GH 19101: empty result, different dtypes
other = IntervalIndex.from_arrays(
    index.left.astype("float64"), index.right, closed=closed
)
result = index.symmetric_difference(other, sort=sort)
expected = empty_index(dtype="float64", closed=closed)
tm.assert_index_equal(result, expected)
