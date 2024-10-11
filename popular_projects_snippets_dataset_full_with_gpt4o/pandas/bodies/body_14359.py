# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py
df = tm.makeDataFrame()

result = tm.round_trip_pathlib(
    lambda p: df.to_hdf(p, "df"), lambda p: read_hdf(p, "df")
)
tm.assert_frame_equal(df, result)
