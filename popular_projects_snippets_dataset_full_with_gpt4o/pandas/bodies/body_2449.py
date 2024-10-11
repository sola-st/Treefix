# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
df = DataFrame({"A": [1, 2, 3]}, dtype="Int64")
orig = df.copy()

df.loc[:] = df.values[:, ::-1]
tm.assert_frame_equal(df, orig)

df.loc[:] = pd.core.arrays.PandasArray(df.values[:, ::-1])
tm.assert_frame_equal(df, orig)

df.iloc[:] = df.iloc[:, :]
tm.assert_frame_equal(df, orig)
