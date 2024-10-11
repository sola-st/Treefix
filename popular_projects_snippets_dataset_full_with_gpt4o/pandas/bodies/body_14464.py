# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_compat.py
path, objname, df = pytables_hdf5_file
result = pd.read_hdf(path, key=objname)
expected = df
tm.assert_frame_equal(result, expected)
