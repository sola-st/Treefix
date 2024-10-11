# Extracted from ./data/repos/pandas/pandas/tests/io/test_feather.py
df = tm.makeDataFrame().reset_index()
result = tm.round_trip_pathlib(df.to_feather, read_feather)
tm.assert_frame_equal(df, result)
