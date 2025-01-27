# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_setops.py
# GH 19101: empty result, same dtype
index = empty_index(dtype="int64", closed=closed)
result = index.union(index, sort=sort)
tm.assert_index_equal(result, index)

# GH 19101: empty result, different numeric dtypes -> common dtype is f8
other = empty_index(dtype="float64", closed=closed)
result = index.union(other, sort=sort)
expected = other
tm.assert_index_equal(result, expected)

other = index.union(index, sort=sort)
tm.assert_index_equal(result, expected)

other = empty_index(dtype="uint64", closed=closed)
result = index.union(other, sort=sort)
tm.assert_index_equal(result, expected)

result = other.union(index, sort=sort)
tm.assert_index_equal(result, expected)
