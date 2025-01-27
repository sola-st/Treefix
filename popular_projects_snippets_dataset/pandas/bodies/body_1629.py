# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#34497
df = DataFrame(
    data=np.array([[1, 2, 3, 4], [5, 6, 7, 8], [1, 2, np.nan, np.nan]]).T,
    columns=["a", "b", "c"],
    dtype="Int64",
)
df2 = df.set_index("c")
assert df2.index.dtype == "Int64"

res = df2.loc[1]
expected = Series([1, 5], index=df2.columns, dtype="Int64", name=1)
tm.assert_series_equal(res, expected)

# pd.NA and duplicates in an object-dtype Index
df2.index = df2.index.astype(object)
res = df2.loc[1]
tm.assert_series_equal(res, expected)
