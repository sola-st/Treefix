# Extracted from ./data/repos/pandas/pandas/tests/io/test_fsspec.py
df = DataFrame({"a": [0]})
df.to_json(
    "testmem://afile",
    compression=compression,
    storage_options={"test": "json_write"},
)
assert fsspectest.test[0] == "json_write"
out = read_json(
    "testmem://afile",
    compression=compression,
    storage_options={"test": "json_read"},
)
assert fsspectest.test[0] == "json_read"
tm.assert_frame_equal(df, out)
