# Extracted from ./data/repos/pandas/pandas/tests/window/test_api.py
df = DataFrame([[1, 2]], columns=["A", "B"])
g = df.rolling(window=5)
with pytest.raises(KeyError, match="Columns not found: 'C'"):
    g[["C"]]
with pytest.raises(KeyError, match="^[^A]+$"):
    # A should not be referenced as a bad column...
    # will have to rethink regex if you change message!
    g[["A", "C"]]
