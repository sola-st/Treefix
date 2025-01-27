# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_numeric.py
idx = self._index_cls([np.nan])
assert not idx.isin([0]).item()
assert not idx.isin([1]).item()
assert idx.isin([np.nan]).item()
