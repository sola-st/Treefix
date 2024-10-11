# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_indexing.py
# case that goes through searchsorted and key is non-comparable to values
arr = np.arange(10**7, dtype=dtype)
idx = Index(arr)
with pytest.raises(KeyError, match="None"):
    idx.get_loc(None)
