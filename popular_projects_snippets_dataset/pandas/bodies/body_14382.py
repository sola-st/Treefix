# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_round_trip.py
path = tmp_path / setup_path

df = tm.makeDataFrame()
df.iloc[:10].to_hdf(path, "df", append=True)
df.iloc[10:].to_hdf(path, "df", append=True, format="table")
tm.assert_frame_equal(read_hdf(path, "df"), df)

# append to False
df.iloc[:10].to_hdf(path, "df", append=False, format="table")
df.iloc[10:].to_hdf(path, "df", append=True)
tm.assert_frame_equal(read_hdf(path, "df"), df)
