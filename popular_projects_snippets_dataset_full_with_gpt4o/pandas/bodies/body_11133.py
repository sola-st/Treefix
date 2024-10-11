# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# GH 11741
msg = r"^'Z'$"
df1 = DataFrame(np.random.randn(1, 4), columns=list("ABCD"))
with pytest.raises(KeyError, match=msg):
    df1.groupby("Z")
df2 = DataFrame(np.random.randn(2, 4), columns=list("ABCD"))
with pytest.raises(KeyError, match=msg):
    df2.groupby("Z")
