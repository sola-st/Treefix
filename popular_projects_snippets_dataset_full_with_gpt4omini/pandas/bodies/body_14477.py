# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_read.py
# GH 37441
# Ensure that the index of the DataFrame is not a view
# into the original recarray that pytables reads in
df = DataFrame(np.random.rand(4, 5), index=[0, 1, 2, 3], columns=list("ABCDE"))

path = tmp_path / setup_path
df.to_hdf(path, "df", mode="w", format="table")

df2 = read_hdf(path, "df")
assert df2.index._data.base is None
tm.assert_frame_equal(df, df2)
