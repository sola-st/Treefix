# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_indexing.py
index = Index([0, 1, 2])
with pytest.raises(InvalidIndexError, match=r"\[1, 2\]"):
    index.get_loc([1, 2])
