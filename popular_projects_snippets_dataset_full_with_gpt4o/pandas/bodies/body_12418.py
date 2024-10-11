# Extracted from ./data/repos/pandas/pandas/tests/io/test_common.py
# GH39247
expected = tm.makeDataFrame()
with tm.ensure_clean() as path:
    with open(path, "wb") as handle:
        with codecs.getwriter("utf-8")(handle) as encoded:
            expected.to_csv(encoded)
    with open(path, "rb") as handle:
        with codecs.getreader("utf-8")(handle) as encoded:
            df = pd.read_csv(encoded, index_col=0)
tm.assert_frame_equal(expected, df)
