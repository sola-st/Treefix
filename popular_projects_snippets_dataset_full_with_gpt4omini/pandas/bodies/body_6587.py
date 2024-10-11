# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_setops.py
# intersect with Index with dtype int64
index = RangeIndex(start=0, stop=20, step=2)
other = Index(np.arange(1, 6))
result = index.intersection(other, sort=sort)
expected = Index(np.sort(np.intersect1d(index.values, other.values)))
tm.assert_index_equal(result, expected)

result = other.intersection(index, sort=sort)
expected = Index(
    np.sort(np.asarray(np.intersect1d(index.values, other.values)))
)
tm.assert_index_equal(result, expected)

# intersect with increasing RangeIndex
other = RangeIndex(1, 6)
result = index.intersection(other, sort=sort)
expected = Index(np.sort(np.intersect1d(index.values, other.values)))
tm.assert_index_equal(result, expected, exact="equiv")

# intersect with decreasing RangeIndex
other = RangeIndex(5, 0, -1)
result = index.intersection(other, sort=sort)
expected = Index(np.sort(np.intersect1d(index.values, other.values)))
tm.assert_index_equal(result, expected, exact="equiv")

# reversed (GH 17296)
result = other.intersection(index, sort=sort)
tm.assert_index_equal(result, expected, exact="equiv")

# GH 17296: intersect two decreasing RangeIndexes
first = RangeIndex(10, -2, -2)
other = RangeIndex(5, -4, -1)
expected = first.astype(int).intersection(other.astype(int), sort=sort)
result = first.intersection(other, sort=sort).astype(int)
tm.assert_index_equal(result, expected)

# reversed
result = other.intersection(first, sort=sort).astype(int)
tm.assert_index_equal(result, expected)

index = RangeIndex(5, name="foo")

# intersect of non-overlapping indices
other = RangeIndex(5, 10, 1, name="foo")
result = index.intersection(other, sort=sort)
expected = RangeIndex(0, 0, 1, name="foo")
tm.assert_index_equal(result, expected)

other = RangeIndex(-1, -5, -1)
result = index.intersection(other, sort=sort)
expected = RangeIndex(0, 0, 1)
tm.assert_index_equal(result, expected)

# intersection of empty indices
other = RangeIndex(0, 0, 1)
result = index.intersection(other, sort=sort)
expected = RangeIndex(0, 0, 1)
tm.assert_index_equal(result, expected)

result = other.intersection(index, sort=sort)
tm.assert_index_equal(result, expected)
