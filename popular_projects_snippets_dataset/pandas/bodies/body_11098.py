# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
grouped = df.groupby("A")
with pytest.raises(TypeError, match="Could not convert"):
    grouped.agg(np.mean)
with pytest.raises(TypeError, match="Could not convert"):
    grouped.mean()

df = df.loc[:, ["A", "C", "D"]]
df["E"] = datetime.now()
grouped = df.groupby("A")
msg = "datetime64 type does not support sum operations"
with pytest.raises(TypeError, match=msg):
    grouped.agg(np.sum)
with pytest.raises(TypeError, match=msg):
    grouped.sum()

# won't work with axis = 1
grouped = df.groupby({"A": 0, "C": 0, "D": 1, "E": 1}, axis=1)
msg = "does not support reduction 'sum'"
with pytest.raises(TypeError, match=msg):
    grouped.agg(lambda x: x.sum(0, numeric_only=False))
