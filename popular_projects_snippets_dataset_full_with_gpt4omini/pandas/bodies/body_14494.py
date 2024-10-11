# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_errors.py
df = DataFrame(np.random.rand(4, 5), index=list("abcd"), columns=list("ABCDE"))

path = tmp_path / setup_path
msg = r"File [\S]* does not exist"
with pytest.raises(OSError, match=msg):
    read_hdf(path, "key")

df.to_hdf(path, "df")
store = HDFStore(path, mode="r")
store.close()

msg = "The HDFStore must be open for reading."
with pytest.raises(OSError, match=msg):
    read_hdf(store, "df")
