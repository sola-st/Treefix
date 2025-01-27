# Extracted from ./data/repos/pandas/pandas/tests/io/test_fsspec.py
"""Regression test for writing to a not-yet-existent GCS Parquet file."""
df = DataFrame({"a": [0]})
df.to_parquet(
    "testmem://test/test.csv",
    engine="pyarrow",
    compression=None,
    storage_options={"test": "parquet_write"},
)
assert fsspectest.test[0] == "parquet_write"
read_parquet(
    "testmem://test/test.csv",
    engine="pyarrow",
    storage_options={"test": "parquet_read"},
)
assert fsspectest.test[0] == "parquet_read"
