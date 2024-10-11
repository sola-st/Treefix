# Extracted from ./data/repos/pandas/pandas/tests/io/test_pickle.py
with tm.ensure_clean(get_random_path) as path:
    df = tm.makeDataFrame()
    df.to_pickle(path, protocol=protocol)
    df2 = pd.read_pickle(path)
    tm.assert_frame_equal(df, df2)
