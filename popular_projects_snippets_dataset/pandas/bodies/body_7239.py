# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_indexing.py
idx = Index([0, 6, 2], dtype=np.uint64)
mask = np.array([False, True, False])
other = np.array([1], dtype=np.int64)

expected = Index([1, 6, 1], dtype=np.uint64)

result = idx.where(mask, other)
tm.assert_index_equal(result, expected)

result = idx.putmask(~mask, other)
tm.assert_index_equal(result, expected)
