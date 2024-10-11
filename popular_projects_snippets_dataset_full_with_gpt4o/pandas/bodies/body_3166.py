# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py

with tm.ensure_clean() as filename:

    df.to_csv(filename, compression=compression, encoding=encoding)
    # test the round trip - to_csv -> read_csv
    result = read_csv(
        filename, compression=compression, index_col=0, encoding=encoding
    )
    tm.assert_frame_equal(df, result)

    # test the round trip using file handle - to_csv -> read_csv
    with get_handle(
        filename, "w", compression=compression, encoding=encoding
    ) as handles:
        df.to_csv(handles.handle, encoding=encoding)
        assert not handles.handle.closed

    result = read_csv(
        filename,
        compression=compression,
        encoding=encoding,
        index_col=0,
    ).squeeze("columns")
    tm.assert_frame_equal(df, result)

    # explicitly make sure file is compressed
    with tm.decompress_file(filename, compression) as fh:
        text = fh.read().decode(encoding or "utf8")
        for col in df.columns:
            assert col in text

    with tm.decompress_file(filename, compression) as fh:
        tm.assert_frame_equal(df, read_csv(fh, index_col=0, encoding=encoding))
