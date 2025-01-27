# Extracted from ./data/repos/pandas/pandas/tests/io/test_compression.py
# GH22004
input = pd.Series([0, 5, -2, 10], name="X")
extension = _compression_to_extension[compression_only]
with tm.ensure_clean("compressed" + extension) as path:
    getattr(input, write_method)(path, **write_kwargs)
    if "squeeze" in read_kwargs:
        kwargs = read_kwargs.copy()
        del kwargs["squeeze"]
        output = read_method(path, compression=compression_only, **kwargs).squeeze(
            "columns"
        )
    else:
        output = read_method(path, compression=compression_only, **read_kwargs)
tm.assert_series_equal(output, input, check_names=False)
