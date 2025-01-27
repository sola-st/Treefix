# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
midx = MultiIndex.from_tuples([("a", 1), ("b", 2)])
msg = (
    "method='nearest' not implemented yet for MultiIndex; "
    "see GitHub issue 9365"
)
with pytest.raises(NotImplementedError, match=msg):
    midx.get_indexer(["a"], method="nearest")
msg = "tolerance not implemented yet for MultiIndex"
with pytest.raises(NotImplementedError, match=msg):
    midx.get_indexer(["a"], method="pad", tolerance=2)
