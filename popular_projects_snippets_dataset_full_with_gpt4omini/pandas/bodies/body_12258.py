# Extracted from ./data/repos/pandas/pandas/tests/io/test_fsspec.py
df = DataFrame({"a": [0]})
df.to_feather("testmem://afile", storage_options={"test": "feather_write"})
assert fsspectest.test[0] == "feather_write"
out = read_feather("testmem://afile", storage_options={"test": "feather_read"})
assert fsspectest.test[0] == "feather_read"
tm.assert_frame_equal(df, out)
