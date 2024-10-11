# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_read.py
# GH13231
df = DataFrame({"i": range(5), "c": Series(list("abacd"), dtype="category")})

path = tmp_path / setup_path
df.to_hdf(path, "df", mode="a", format="table")
reread = read_hdf(path)
tm.assert_frame_equal(df, reread)
df.to_hdf(path, "df2", mode="a", format="table")

msg = "key must be provided when HDF5 file contains multiple datasets."
with pytest.raises(ValueError, match=msg):
    read_hdf(path)
