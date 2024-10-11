# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
# writing version 117 requires seek and cannot be used with gzip
df = tm.makeDataFrame()
df.index.name = "index"
with tm.ensure_clean() as path:
    with gzip.GzipFile(path, "wb") as gz:
        df.to_stata(gz, version=114)
    with gzip.GzipFile(path, "rb") as gz:
        reread = read_stata(gz, index_col="index")
tm.assert_frame_equal(df, reread)
