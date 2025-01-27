# Extracted from ./data/repos/pandas/pandas/tests/io/test_pickle.py
df = tm.makeDataFrame()
result = tm.round_trip_localpath(df.to_pickle, pd.read_pickle)
tm.assert_frame_equal(df, result)
