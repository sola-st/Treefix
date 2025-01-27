# Extracted from ./data/repos/pandas/pandas/tests/io/test_common.py
extension, expected = compression_format
path = path_type("foo/bar.csv" + extension)
compression = icom.infer_compression(path, compression="infer")
assert compression == expected
