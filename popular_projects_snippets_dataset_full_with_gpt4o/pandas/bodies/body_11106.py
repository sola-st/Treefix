# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
df = mframe.T
df["baz", "two"] = "peekaboo"

keys = [np.array([0, 0, 1]), np.array([0, 0, 1])]
with pytest.raises(TypeError, match="Could not convert"):
    df.groupby(keys).agg(np.mean)
agged = df.drop(columns=("baz", "two")).groupby(keys).agg(np.mean)
assert isinstance(agged.columns, MultiIndex)

def aggfun(ser):
    if ser.name == ("foo", "one"):
        raise TypeError("Test error message")
    exit(ser.sum())

with pytest.raises(TypeError, match="Test error message"):
    df.groupby(keys).aggregate(aggfun)
