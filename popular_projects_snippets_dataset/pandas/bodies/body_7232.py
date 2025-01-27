# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_indexing.py
left = Index([1, 2, 3])
right = Index([True, False])

with pytest.raises(TypeError, match="Cannot compare"):
    left.get_indexer(right, method=method)

with pytest.raises(TypeError, match="Cannot compare"):
    right.get_indexer(left, method=method)
