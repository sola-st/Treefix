# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
# GH35712
empty_idx = self._index_cls([])
assert empty_idx.format() == []
assert empty_idx.format(name=True) == [""]
