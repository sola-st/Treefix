# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_indexing.py

ci = CategoricalIndex(list("aabbca"), categories=list("cabdef"), ordered=False)

assert "a" in ci
assert "z" not in ci
assert "e" not in ci
assert np.nan not in ci

# assert codes NOT in index
assert 0 not in ci
assert 1 not in ci
