# Extracted from ./data/repos/pandas/pandas/tests/io/test_fsspec.py
text = str(df1.to_csv(index=False)).encode()
with cleared_fs.open("test/test.csv", "wb") as w:
    w.write(text)
df2 = read_csv("memory://test/test.csv", parse_dates=["dt"])

tm.assert_frame_equal(df1, df2)
