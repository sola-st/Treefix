# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_categorical.py
# GH 12531
df = DataFrame(np.random.randn(3, 3), index=list("ABC"), columns=list("XYZ"))
cdf = df.copy()
cdf.index = CategoricalIndex(df.index)
cdf.columns = CategoricalIndex(df.columns)

expect = Series(df.loc["A", :], index=cdf.columns, name="A")
tm.assert_series_equal(cdf.loc["A", :], expect)

expect = Series(df.loc[:, "X"], index=cdf.index, name="X")
tm.assert_series_equal(cdf.loc[:, "X"], expect)

exp_index = CategoricalIndex(list("AB"), categories=["A", "B", "C"])
expect = DataFrame(df.loc[["A", "B"], :], columns=cdf.columns, index=exp_index)
tm.assert_frame_equal(cdf.loc[["A", "B"], :], expect)

exp_columns = CategoricalIndex(list("XY"), categories=["X", "Y", "Z"])
expect = DataFrame(df.loc[:, ["X", "Y"]], index=cdf.index, columns=exp_columns)
tm.assert_frame_equal(cdf.loc[:, ["X", "Y"]], expect)
