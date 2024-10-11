# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
df = DataFrame(
    [[0.123456, 0.234567, 0.567567], [12.32112, 123123.2, 321321.2]],
    index=["A", "B"],
    columns=["X", "Y", "Z"],
)
df.index.name = "index"

with tm.ensure_clean() as path:

    df.to_stata(path, compression=compression)
    reread = read_stata(path, compression=compression, index_col="index")
    tm.assert_frame_equal(df, reread)

    # explicitly ensure file was compressed.
    with tm.decompress_file(path, compression) as fh:
        contents = io.BytesIO(fh.read())
    reread = read_stata(contents, index_col="index")
    tm.assert_frame_equal(df, reread)
