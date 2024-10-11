# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
df = DataFrame([[1, 2]], columns=["A", "B"])
g = df.groupby("A")
with pytest.raises(KeyError, match="\"Columns not found: 'C'\""):
    g[["C"]]

with pytest.raises(KeyError, match="^[^A]+$"):
    # A should not be referenced as a bad column...
    # will have to rethink regex if you change message!
    g[["A", "C"]]
