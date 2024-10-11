# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_file_handling.py
# read_hdf uses default mode
df = tm.makeTimeDataFrame()
path = tmp_path / setup_path
df.to_hdf(path, "df", mode="w")
result = read_hdf(path, "df")
tm.assert_frame_equal(result, df)
