# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_compression.py
df = pd.DataFrame(
    [[0.123456, 0.234567, 0.567567], [12.32112, 123123.2, 321321.2]],
    index=["A", "B"],
    columns=["X", "Y", "Z"],
)

with tm.ensure_clean() as path:
    df.to_json(path, compression=compression)
    tm.assert_frame_equal(df, pd.read_json(path, compression=compression))

    # explicitly ensure file was compressed.
    with tm.decompress_file(path, compression) as fh:
        result = fh.read().decode("utf8")
    tm.assert_frame_equal(df, pd.read_json(result))
