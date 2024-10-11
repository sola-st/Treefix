# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_read.py
path = tmp_path / setup_path
store = HDFStore(path)
store.close()
msg = re.escape(
    "Dataset(s) incompatible with Pandas data types, not table, or no "
    "datasets found in HDF5 file."
)
with pytest.raises(ValueError, match=msg):
    read_hdf(path)
