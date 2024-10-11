# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_read.py
# GH10443
df = DataFrame(np.random.rand(4, 5), index=list("abcd"), columns=list("ABCDE"))

# Categorical dtype not supported for "fixed" format. So no need
# to test with that dtype in the dataframe here.
path = tmp_path / setup_path
df.to_hdf(path, "df", mode="a")
reread = read_hdf(path)
tm.assert_frame_equal(df, reread)
df.to_hdf(path, "df2", mode="a")

msg = "key must be provided when HDF5 file contains multiple datasets."
with pytest.raises(ValueError, match=msg):
    read_hdf(path)
