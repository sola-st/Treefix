# Extracted from ./data/repos/pandas/pandas/tests/io/test_fsspec.py
df1.to_csv("memory://test/test.csv", index=True)

df2 = read_csv("memory://test/test.csv", parse_dates=["dt"], index_col=0)

tm.assert_frame_equal(df1, df2)
