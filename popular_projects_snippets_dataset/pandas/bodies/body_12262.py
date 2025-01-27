# Extracted from ./data/repos/pandas/pandas/tests/io/test_fsspec.py
df = DataFrame({"a": [0]})
df.to_markdown("testmem://afile", storage_options={"test": "md_write"})
assert fsspectest.test[0] == "md_write"
assert fsspectest.cat("testmem://afile")
