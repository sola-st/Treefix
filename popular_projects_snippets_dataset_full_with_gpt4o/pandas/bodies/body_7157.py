# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_numeric.py
index = self._index_cls([1.5, 2.5, 3.5])
assert index.dtype == np.float64
