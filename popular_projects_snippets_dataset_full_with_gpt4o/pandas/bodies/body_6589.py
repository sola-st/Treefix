# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_setops.py
# corner case, Index with non-int64 dtype
index = RangeIndex(start=0, stop=20, step=2)
other = Index([datetime.now() + timedelta(i) for i in range(4)], dtype=object)
result = index.union(other, sort=sort)
expected = Index(np.concatenate((index, other)))
tm.assert_index_equal(result, expected)

result = other.union(index, sort=sort)
expected = Index(np.concatenate((other, index)))
tm.assert_index_equal(result, expected)
