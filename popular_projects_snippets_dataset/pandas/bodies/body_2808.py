# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
dr = date_range("2013-08-01", periods=6, freq="B")
data = np.random.randn(6, 1)
df = DataFrame(data, index=dr, columns=list("A"))
df_rev = DataFrame(data, index=dr[[3, 4, 5] + [0, 1, 2]], columns=list("A"))
# index is not monotonic increasing or decreasing
msg = "index must be monotonic increasing or decreasing"
with pytest.raises(ValueError, match=msg):
    df_rev.reindex(df.index, method="pad")
with pytest.raises(ValueError, match=msg):
    df_rev.reindex(df.index, method="ffill")
with pytest.raises(ValueError, match=msg):
    df_rev.reindex(df.index, method="bfill")
with pytest.raises(ValueError, match=msg):
    df_rev.reindex(df.index, method="nearest")
