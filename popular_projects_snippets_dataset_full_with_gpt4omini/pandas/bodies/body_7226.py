# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_indexing.py
# GH10411
index = Index(np.arange(10))

with pytest.raises(ValueError, match="tolerance argument"):
    index.get_indexer([1, 0], tolerance=1)

with pytest.raises(ValueError, match="limit argument"):
    index.get_indexer([1, 0], limit=1)
