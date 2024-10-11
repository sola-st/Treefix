# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_read.py
# GH 25766
path = tmp_path / setup_path
df = DataFrame({"a": range(2), "b": range(2)})
df.to_hdf(path, "k1")

with pytest.raises(KeyError, match="'No object named k2 in the file'"):
    read_hdf(path, "k2")

# smoke test to test that file is properly closed after
# read with KeyError before another write
df.to_hdf(path, "k2")
