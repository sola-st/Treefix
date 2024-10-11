# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_read.py
# GH10330
# No check for non-string path_or-buf, and no test of open store
df = DataFrame(np.random.rand(4, 5), index=list("abcd"), columns=list("ABCDE"))
df.index.name = "letters"
df = df.set_index(keys="E", append=True)

path = tmp_path / setup_path
df.to_hdf(path, "df", mode="w")
direct = read_hdf(path, "df")
with HDFStore(path, mode="r") as store:
    indirect = read_hdf(store, "df")
    tm.assert_frame_equal(direct, indirect)
    assert store.is_open
