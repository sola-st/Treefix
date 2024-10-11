# Extracted from ./data/repos/pandas/pandas/tests/io/test_fsspec.py
df = DataFrame({"a": [0]})
df.to_stata(
    "testmem://afile", storage_options={"test": "stata_write"}, write_index=False
)
assert fsspectest.test[0] == "stata_write"
out = read_stata("testmem://afile", storage_options={"test": "stata_read"})
assert fsspectest.test[0] == "stata_read"
tm.assert_frame_equal(df, out.astype("int64"))
