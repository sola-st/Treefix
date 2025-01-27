# Extracted from ./data/repos/pandas/pandas/tests/io/test_common.py
# GH39247
expected = tm.makeDataFrame()
with tm.ensure_clean() as path:
    with codecs.open(path, mode="w", encoding=encoding) as handle:
        getattr(expected, f"to_{format}")(handle)
    with codecs.open(path, mode="r", encoding=encoding) as handle:
        if format == "csv":
            df = pd.read_csv(handle, index_col=0)
        else:
            df = pd.read_json(handle)
tm.assert_frame_equal(expected, df)
