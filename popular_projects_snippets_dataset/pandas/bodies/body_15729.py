# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_to_csv.py

with tm.ensure_clean() as filename:

    s.to_csv(filename, compression=compression, encoding=encoding, header=True)
    # test the round trip - to_csv -> read_csv
    result = pd.read_csv(
        filename,
        compression=compression,
        encoding=encoding,
        index_col=0,
    ).squeeze("columns")
    tm.assert_series_equal(s, result)

    # test the round trip using file handle - to_csv -> read_csv
    with get_handle(
        filename, "w", compression=compression, encoding=encoding
    ) as handles:
        s.to_csv(handles.handle, encoding=encoding, header=True)

    result = pd.read_csv(
        filename,
        compression=compression,
        encoding=encoding,
        index_col=0,
    ).squeeze("columns")
    tm.assert_series_equal(s, result)

    # explicitly ensure file was compressed
    with tm.decompress_file(filename, compression) as fh:
        text = fh.read().decode(encoding or "utf8")
        assert s.name in text

    with tm.decompress_file(filename, compression) as fh:
        tm.assert_series_equal(
            s,
            pd.read_csv(fh, index_col=0, encoding=encoding).squeeze("columns"),
        )
