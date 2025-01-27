# Extracted from ./data/repos/pandas/pandas/tests/io/test_pickle.py
# GH#39002
df = pd.DataFrame(range(100000))
result = tm.round_trip_pathlib(
    partial(df.to_pickle, protocol=protocol, compression=compression),
    partial(pd.read_pickle, compression=compression),
)
tm.assert_frame_equal(df, result)
