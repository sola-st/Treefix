# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rename_axis.py
# GH#17833
df = DataFrame({"A": [1, 2], "B": [1, 2]})
with pytest.raises(ValueError, match="Use `.rename`"):
    df.rename_axis(id, axis=0)

with pytest.raises(ValueError, match="Use `.rename`"):
    df.rename_axis({0: 10, 1: 20}, axis=0)

with pytest.raises(ValueError, match="Use `.rename`"):
    df.rename_axis(id, axis=1)

with pytest.raises(ValueError, match="Use `.rename`"):
    df["A"].rename_axis(id)
