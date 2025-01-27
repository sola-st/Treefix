# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_numeric.py
idx = self._index_cls([1.0, 2.0])
assert idx.equals(other)
assert other.equals(idx)
