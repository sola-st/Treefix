# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_indexing.py
index1 = Index([1, 2, 3, 4, 5])
index2 = Index([2, 4, 6])

if reverse:
    index1 = index1[::-1]
    expected = expected[::-1]

result = index2.get_indexer(index1, method=method)
tm.assert_almost_equal(result, expected)
