# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
df = DataFrame(
    np.random.randn(5, 3),
    index=["a", "b", "c", "d", "e"],
    columns=["foo", "bar", "baz"],
)

df["timestamp"] = Timestamp("20010102")

# check our dtypes
result = df.dtypes
expected = Series(
    [np.dtype("float64")] * 3 + [np.dtype("datetime64[ns]")],
    index=["foo", "bar", "baz", "timestamp"],
)
tm.assert_series_equal(result, expected)

# GH#16674 iNaT is treated as an integer when given by the user
df.loc["b", "timestamp"] = iNaT
assert not isna(df.loc["b", "timestamp"])
assert df["timestamp"].dtype == np.object_
assert df.loc["b", "timestamp"] == iNaT

# allow this syntax (as of GH#3216)
df.loc["c", "timestamp"] = np.nan
assert isna(df.loc["c", "timestamp"])

# allow this syntax
df.loc["d", :] = np.nan
assert not isna(df.loc["c", :]).all()
