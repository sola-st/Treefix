# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_compat.py
path, objname, df = pytables_hdf5_file
# This is a regression test for pandas-dev/pandas/issues/11188
result = pd.read_hdf(path, key=objname, start=1)
expected = df[1:].reset_index(drop=True)
tm.assert_frame_equal(result, expected)
