# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
df = DataFrame({"a": [1, 2, 3], "b": [3, 4, 5]}, index=[1.0, 2.0, 3.0])
df2 = df.copy()
df.loc[df.index] = df.loc[df.index]
tm.assert_frame_equal(df, df2)
