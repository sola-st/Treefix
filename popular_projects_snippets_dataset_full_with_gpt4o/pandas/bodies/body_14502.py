# Extracted from ./data/repos/pandas/pandas/tests/io/test_compression.py
# GH22004
input = pd.DataFrame([[1.0, 0, -4], [3.4, 5, 2]], columns=["X", "Y", "Z"])
extension = _compression_to_extension[compression_only]
with tm.ensure_clean("compressed" + extension) as path:
    getattr(input, write_method)(path, **write_kwargs)
    output = read_method(path, compression=compression_only)
tm.assert_frame_equal(output, input)
