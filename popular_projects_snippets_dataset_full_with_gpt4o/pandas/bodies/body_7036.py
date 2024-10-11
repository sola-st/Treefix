# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_indexing.py
ci = CategoricalIndex(list("aabbca") + [np.nan], categories=list("cabdef"))
assert np.nan in ci
