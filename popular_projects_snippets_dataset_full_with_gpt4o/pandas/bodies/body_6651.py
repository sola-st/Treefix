# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py
# GH35712
empty_idx = self._index_cls(0)
assert empty_idx.format() == []
assert empty_idx.format(name=True) == [""]
