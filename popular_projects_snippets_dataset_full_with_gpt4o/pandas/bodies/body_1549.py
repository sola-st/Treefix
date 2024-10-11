# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
df = DataFrame(
    np.random.randn(5, 3),
    index=["a", "b", "c", "d", "e"],
    columns=["foo", "bar", "baz"],
)
df["str"] = "qux"
df.loc[df.index[::2], "str"] = np.nan
expected = np.array([np.nan, "qux", np.nan, "qux", np.nan], dtype=object)
tm.assert_almost_equal(df["str"].values, expected)
