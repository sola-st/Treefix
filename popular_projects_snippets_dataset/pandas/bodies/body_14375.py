# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_store.py
# GH#48667
df = DataFrame([[1]], columns=[True], index=Index([False], dtype="bool"))
expected = df.copy()

# # Test to make sure defaults are to not drop.
# # Corresponding to Issue 9382
path = tmp_path / setup_path
df.to_hdf(path, "a")
result = read_hdf(path, "a")
tm.assert_frame_equal(expected, result)
