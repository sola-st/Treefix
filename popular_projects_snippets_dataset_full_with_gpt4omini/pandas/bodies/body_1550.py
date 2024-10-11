# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#7704
# dtype conversion on setting
df = DataFrame(np.random.rand(30, 3), columns=tuple("ABC"))
df["event"] = np.nan
df.loc[10, "event"] = "foo"
result = df.dtypes
expected = Series(
    [np.dtype("float64")] * 3 + [np.dtype("object")],
    index=["A", "B", "C", "event"],
)
tm.assert_series_equal(result, expected)
