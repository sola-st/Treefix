# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_setops.py
# TODO(GH#25151): decide on True behaviour
# # sort=True
idx = MultiIndex.from_product([[1, pd.Timestamp("2000")], ["a", "b"]])
with pytest.raises(TypeError, match="Cannot compare"):
    idx.union(idx[:1], sort=True)
