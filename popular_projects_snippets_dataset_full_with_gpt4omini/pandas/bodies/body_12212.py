# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_compression.py
parser, data, expected = parser_and_data
compress_type = compression_only

ext = _compression_to_extension[compress_type]
filename = filename if filename is None else filename.format(ext=ext)

if filename and buffer:
    request.node.add_marker(
        pytest.mark.xfail(
            reason="Cannot deduce compression from buffer of compressed data."
        )
    )

with tm.ensure_clean(filename=filename) as path:
    tm.write_to_compressed(compress_type, path, data)
    compression = "infer" if filename else compress_type

    if buffer:
        with open(path, "rb") as f:
            result = parser.read_csv(f, compression=compression)
    else:
        result = parser.read_csv(path, compression=compression)

    tm.assert_frame_equal(result, expected)
