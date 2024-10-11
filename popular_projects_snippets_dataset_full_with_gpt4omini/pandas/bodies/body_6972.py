# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
ci = CategoricalIndex([1, 2, np.nan])
assert ci.categories.dtype.kind == "i"

idx = Index([1, 2])

result = idx.union(ci)
expected = Index([1, 2, np.nan], dtype=np.float64)
tm.assert_index_equal(result, expected)

result = ci.union(idx)
tm.assert_index_equal(result, expected)
