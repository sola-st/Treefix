# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_setops.py
# https://github.com/pandas-dev/pandas/issues/26778
index = RangeIndex(start=0, stop=3)
other = Index([0.5, 1.5], dtype=np.float64)
result = index.union(other)
expected = Index([0.0, 0.5, 1, 1.5, 2.0], dtype=np.float64)
tm.assert_index_equal(result, expected)

result = other.union(index)
tm.assert_index_equal(result, expected)
