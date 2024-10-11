# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_read.py
df = DataFrame(np.random.rand(4, 5), index=list("abcd"), columns=list("ABCDE"))
df.index.name = "letters"
df = df.set_index(keys="E", append=True)

path = tmp_path / setup_path
df.to_hdf(path, "df", mode="w", format="t")
direct = read_hdf(path, "df")
iterator = read_hdf(path, "df", iterator=True)
with closing(iterator.store):
    assert isinstance(iterator, TableIterator)
    indirect = next(iterator.__iter__())
    tm.assert_frame_equal(direct, indirect)
