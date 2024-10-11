# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
df = DataFrame(np.random.randn(8, 4), columns=["A", "B", "C", "D"])
df["key"] = ["foo", "bar"] * 4
df1 = df.loc[:, ["A", "B"]]
df2 = df.loc[:, ["C", "D"]]
df3 = df.loc[:, ["key"]]

result = df1.join([df2, df3])
tm.assert_frame_equal(result, df)
