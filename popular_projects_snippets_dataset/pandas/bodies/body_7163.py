# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_numeric.py
index_cls = self._index_cls

idx = index_cls([1.0, 2.0])
assert idx.equals(idx)
assert idx.identical(idx)

idx2 = index_cls([1.0, 2.0])
assert idx.equals(idx2)

idx = index_cls([1.0, np.nan])
assert idx.equals(idx)
assert idx.identical(idx)

idx2 = index_cls([1.0, np.nan])
assert idx.equals(idx2)
