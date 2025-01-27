# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
grouped = three_group.groupby(["A", "B"])
with pytest.raises(TypeError, match="Could not convert"):
    grouped.agg(np.mean)
with pytest.raises(TypeError, match="Could not convert"):
    grouped.mean()
