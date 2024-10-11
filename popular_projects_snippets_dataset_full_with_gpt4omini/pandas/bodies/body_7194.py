# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_numeric.py
# GH#44609 cases where we don't retain dtype
idx = Index([1, 2, 3], dtype=np.uint64)
result = idx.map(lambda x: -x)
expected = Index([-1, -2, -3], dtype=np.int64)
tm.assert_index_equal(result, expected)
