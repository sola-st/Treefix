# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
# GH 14885
s = Series(
    range(8),
    index=MultiIndex.from_product([["a", "b"], ["c", "d"], ["e", "f"]]),
)

with pytest.raises(KeyError, match=r"^\('a', 'b'\)$"):
    s.loc["a", "b"]
with pytest.raises(KeyError, match=r"^\('a', 'd', 'g'\)$"):
    s.loc["a", "d", "g"]
with pytest.raises(IndexingError, match="Too many indexers"):
    s.loc["a", "d", "g", "j"]
