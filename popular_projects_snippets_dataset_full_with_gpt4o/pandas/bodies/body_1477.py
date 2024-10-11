# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
s = Series(range(3), index=["a", "b", "c"])

# consistency
with pytest.raises(KeyError, match="not in index"):
    s[["a", "d"]]

s = Series(range(3))
with pytest.raises(KeyError, match="not in index"):
    s[[0, 3]]
