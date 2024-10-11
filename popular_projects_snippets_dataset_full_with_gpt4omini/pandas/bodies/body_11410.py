# Extracted from ./data/repos/pandas/pandas/tests/io/test_pickle.py
with tm.ensure_clean() as path:
    df = tm.makeDataFrame()
    with open(path, "wb") as fh:
        df.to_pickle(fh)
    with open(path, "rb") as fh:
        result = pd.read_pickle(fh)
    tm.assert_frame_equal(df, result)
