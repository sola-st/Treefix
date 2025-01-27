# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_period.py
# GH35712
empty_idx = self._index_cls([], freq="A")
assert empty_idx.format() == []
assert empty_idx.format(name=True) == [""]
