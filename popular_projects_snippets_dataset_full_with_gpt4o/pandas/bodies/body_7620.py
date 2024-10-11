# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
midx = MultiIndex.from_product([["A", "B"], [1, 2]])
assert "A" in midx
assert "A" not in midx._engine
