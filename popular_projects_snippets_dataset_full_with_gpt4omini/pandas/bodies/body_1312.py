# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_categorical.py

# non-unique
df = DataFrame(np.random.randn(3, 3), index=list("ABA"), columns=list("XYX"))
cdf = df.copy()
cdf.index = CategoricalIndex(df.index)
cdf.columns = CategoricalIndex(df.columns)

exp_index = CategoricalIndex(list("AA"), categories=["A", "B"])
expect = DataFrame(df.loc["A", :], columns=cdf.columns, index=exp_index)
tm.assert_frame_equal(cdf.loc["A", :], expect)

exp_columns = CategoricalIndex(list("XX"), categories=["X", "Y"])
expect = DataFrame(df.loc[:, "X"], index=cdf.index, columns=exp_columns)
tm.assert_frame_equal(cdf.loc[:, "X"], expect)

expect = DataFrame(
    df.loc[["A", "B"], :],
    columns=cdf.columns,
    index=CategoricalIndex(list("AAB")),
)
tm.assert_frame_equal(cdf.loc[["A", "B"], :], expect)

expect = DataFrame(
    df.loc[:, ["X", "Y"]],
    index=cdf.index,
    columns=CategoricalIndex(list("XXY")),
)
tm.assert_frame_equal(cdf.loc[:, ["X", "Y"]], expect)
