# Extracted from ./data/repos/pandas/pandas/tests/io/test_pickle.py
with tm.ensure_clean():
    mockurl = "memory://afile"
    df = tm.makeDataFrame()
    df.to_pickle(mockurl)
    result = pd.read_pickle(mockurl)
    tm.assert_frame_equal(df, result)
