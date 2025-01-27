# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_setops.py
# corner case, non-numeric
index = Index(np.arange(5, dtype=dtype), dtype=dtype)
assert index.dtype == dtype

other = Index([datetime.now() + timedelta(i) for i in range(4)], dtype=object)
result = index.union(other)
expected = Index(np.concatenate((index, other)))
tm.assert_index_equal(result, expected)

result = other.union(index)
expected = Index(np.concatenate((other, index)))
tm.assert_index_equal(result, expected)
