# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
# GH 22060
df = DataFrame(columns=["a", "b", "c"]).astype(
    {"a": "datetime64[ns]", "b": np.int64, "c": np.float64}
)
df1 = df.set_index(["a"])
df1["d"] = []
result = df1.reset_index()
expected = DataFrame(columns=["a", "b", "c", "d"], index=range(0)).astype(
    {"a": "datetime64[ns]", "b": np.int64, "c": np.float64, "d": np.float64}
)
tm.assert_frame_equal(result, expected)

df2 = df.set_index(["a", "b"])
df2["d"] = []
result = df2.reset_index()
tm.assert_frame_equal(result, expected)
