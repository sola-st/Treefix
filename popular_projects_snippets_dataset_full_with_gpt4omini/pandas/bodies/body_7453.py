# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_setops.py
# GH 13490
idx = MultiIndex.from_product([["a", "b"], ["A", "B"]], names=["a", "b"])
result = idx.symmetric_difference(idx)
assert result.names == idx.names

idx2 = idx.copy().rename(["A", "B"])
result = idx.symmetric_difference(idx2)
assert result.names == [None, None]
