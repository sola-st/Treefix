# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
# convert to utc
df = DataFrame(np.random.randn(2, 1), columns=["A"])
df["B"] = idx
df["B"] = idx.to_series(index=[0, 1]).dt.tz_convert(None)

result = df["B"]
comp = Series(idx.tz_convert("UTC").tz_localize(None), name="B")
tm.assert_series_equal(result, comp)
