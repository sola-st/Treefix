# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_read_fwf.py
data = """1111111111
    2222222222
    3333333333""".strip()

compression = compression_only
extension = _compression_to_extension[compression]

kwargs = {"widths": [5, 5], "names": ["one", "two"]}
expected = read_fwf(StringIO(data), **kwargs)

data = bytes(data, encoding="utf-8")

with tm.ensure_clean(filename="tmp." + extension) as path:
    tm.write_to_compressed(compression, path, data)

    if infer is not None:
        kwargs["compression"] = "infer" if infer else compression

    result = read_fwf(path, **kwargs)
    tm.assert_frame_equal(result, expected)
