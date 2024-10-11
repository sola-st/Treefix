# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_indexing.py
index1 = Index([1, 2, 3, 4, 5])
index2 = Index([2, 4, 6])

r1 = index1.get_indexer(index2)
e1 = np.array([1, 3, -1], dtype=np.intp)
tm.assert_almost_equal(r1, e1)
