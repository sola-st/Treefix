# Extracted from ./data/repos/pandas/pandas/tests/io/test_pickle.py
"""
    Read/write from binary file-objects w/wo compression.

    GH 26237, GH 29054, and GH 29570
    """
df = tm.makeDataFrame()

# reference for compression
with tm.ensure_clean() as path:
    df.to_pickle(path, compression=compression)
    reference = Path(path).read_bytes()

# write
buffer = io.BytesIO()
df.to_pickle(buffer, compression=compression)
buffer.seek(0)

# gzip  and zip safe the filename: cannot compare the compressed content
assert buffer.getvalue() == reference or compression in ("gzip", "zip", "tar")

# read
read_df = pd.read_pickle(buffer, compression=compression)
buffer.seek(0)
tm.assert_frame_equal(df, read_df)
