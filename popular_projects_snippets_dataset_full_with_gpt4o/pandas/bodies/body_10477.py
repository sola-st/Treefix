# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_filters.py
df = DataFrame({"A": np.arange(8), "B": list("aabbbbcc"), "C": np.arange(8)})
s = df["B"]
g_df = df.groupby("B")
g_s = s.groupby(s)

f = lambda x: x
msg = "filter function returned a DataFrame, but expected a scalar bool"
with pytest.raises(TypeError, match=msg):
    g_df.filter(f)
msg = "the filter must return a boolean result"
with pytest.raises(TypeError, match=msg):
    g_s.filter(f)

f = lambda x: x == 1
msg = "filter function returned a DataFrame, but expected a scalar bool"
with pytest.raises(TypeError, match=msg):
    g_df.filter(f)
msg = "the filter must return a boolean result"
with pytest.raises(TypeError, match=msg):
    g_s.filter(f)

f = lambda x: np.outer(x, x)
msg = "can't multiply sequence by non-int of type 'str'"
with pytest.raises(TypeError, match=msg):
    g_df.filter(f)
msg = "the filter must return a boolean result"
with pytest.raises(TypeError, match=msg):
    g_s.filter(f)
