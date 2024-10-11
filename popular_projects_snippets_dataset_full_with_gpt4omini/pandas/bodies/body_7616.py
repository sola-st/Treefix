# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# GH#35878
idx = MultiIndex.from_tuples([("a", 1), ("b", 2)])
msg = r"\[\]"
with pytest.raises(InvalidIndexError, match=msg):
    idx.get_loc([])
