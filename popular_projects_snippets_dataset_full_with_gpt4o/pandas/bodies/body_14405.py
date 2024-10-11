# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_round_trip.py
# GH 9330
df = DataFrame({"B": [1, 2], "A": ["x", "y"]})

path = tmp_path / setup_path
df.to_hdf(path, "df", format="table")
other = read_hdf(path, "df")
tm.assert_frame_equal(df, other)
assert df.equals(other)
assert other.equals(df)
