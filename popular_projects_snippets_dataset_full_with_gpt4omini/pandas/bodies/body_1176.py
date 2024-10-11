# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_partial.py
# no index to start
expected = DataFrame({0: Series(1, index=range(4))}, columns=["A", "B", 0])

df = DataFrame(columns=["A", "B"])
df[0] = Series(1, index=range(4))
df.dtypes
str(df)
tm.assert_frame_equal(df, expected)

df = DataFrame(columns=["A", "B"])
df.loc[:, 0] = Series(1, index=range(4))
df.dtypes
str(df)
tm.assert_frame_equal(df, expected)
