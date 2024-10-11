# Extracted from ./data/repos/pandas/pandas/tests/frame/test_subclass.py
index = ["a", "b", "c", "d", "e"]
columns = ["one", "two", "three", "four"]
df1 = tm.SubclassedDataFrame(
    np.random.randn(5, 4), index=index, columns=columns
)
df2 = tm.SubclassedDataFrame(
    np.random.randn(4, 4), index=index[:4], columns=columns
)
correls = df1.corrwith(df2, axis=1, drop=True, method="kendall")

assert isinstance(correls, (tm.SubclassedSeries))
