# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_partial.py
# columns will align
df = DataFrame(columns=["A", "B"])
df.loc[0] = Series(1, index=range(4))
expected = DataFrame(columns=["A", "B"], index=[0], dtype=np.float64)
tm.assert_frame_equal(df, expected)

# columns will align
df = DataFrame(columns=["A", "B"])
df.loc[0] = Series(1, index=["B"])

exp = DataFrame([[np.nan, 1]], columns=["A", "B"], index=[0], dtype="float64")
tm.assert_frame_equal(df, exp)
