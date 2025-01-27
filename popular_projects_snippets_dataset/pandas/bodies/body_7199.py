# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_setops.py
# https://github.com/pandas-dev/pandas/issues/26778
# [u]int | float -> float
index = Index([0, 2, 3], dtype=dtype)
other = Index([0.5, 1.5], dtype=np.float64)
expected = Index([0.0, 0.5, 1.5, 2.0, 3.0], dtype=np.float64)
result = index.union(other)
tm.assert_index_equal(result, expected)

result = other.union(index)
tm.assert_index_equal(result, expected)
