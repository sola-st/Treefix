# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
df = DataFrame(
    np.random.randn(5, 3), index=np.arange(5), columns=["c", "b", "a"]
)
df.insert(0, "foo", df["a"])
df.insert(2, "bar", df["c"])

# diff dtype

# new item
df["x"] = df["a"].astype("float32")
result = df.dtypes
expected = Series(
    [np.dtype("float64")] * 5 + [np.dtype("float32")],
    index=["foo", "c", "bar", "b", "a", "x"],
)
tm.assert_series_equal(result, expected)

# replacing current (in different block)
df["a"] = df["a"].astype("float32")
result = df.dtypes
expected = Series(
    [np.dtype("float64")] * 4 + [np.dtype("float32")] * 2,
    index=["foo", "c", "bar", "b", "a", "x"],
)
tm.assert_series_equal(result, expected)

df["y"] = df["a"].astype("int32")
result = df.dtypes
expected = Series(
    [np.dtype("float64")] * 4 + [np.dtype("float32")] * 2 + [np.dtype("int32")],
    index=["foo", "c", "bar", "b", "a", "x", "y"],
)
tm.assert_series_equal(result, expected)
