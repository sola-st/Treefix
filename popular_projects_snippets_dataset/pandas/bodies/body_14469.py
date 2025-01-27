# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_read.py
# GH 28699
path = tmp_path / setup_path
df = DataFrame({"a": range(2), "b": range(2)})
df.to_hdf(path, "k1")

with HDFStore(path, "r") as store:

    with pytest.raises(KeyError, match="'No object named k2 in the file'"):
        read_hdf(store, "k2")

    # Test that the file is still open after a KeyError and that we can
    # still read from it.
    read_hdf(store, "k1")
