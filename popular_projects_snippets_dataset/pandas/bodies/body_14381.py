# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_round_trip.py

# GH4584
# API issue when to_hdf doesn't accept append AND format args
path = tmp_path / setup_path

df = tm.makeDataFrame()
df.iloc[:10].to_hdf(path, "df", append=True, format="table")
df.iloc[10:].to_hdf(path, "df", append=True, format="table")
tm.assert_frame_equal(read_hdf(path, "df"), df)

# append to False
df.iloc[:10].to_hdf(path, "df", append=False, format="table")
df.iloc[10:].to_hdf(path, "df", append=True, format="table")
tm.assert_frame_equal(read_hdf(path, "df"), df)
