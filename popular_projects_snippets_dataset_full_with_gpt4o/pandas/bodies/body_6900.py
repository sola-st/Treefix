# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_setops.py
# TODO(GH#25151): decide on True behaviour
# sort=True
idx = Index([1, pd.Timestamp("2000")])
with pytest.raises(TypeError, match=".*"):
    idx.union(idx[:1], sort=True)
