# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
# GH 17328
df = tm.makeDataFrame()
df.index.name = "index"
with tm.ensure_clean() as path:
    df.to_stata(path)
    reread = read_stata(path, index_col="index")
tm.assert_frame_equal(df, reread)
