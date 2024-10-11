# Extracted from ./data/repos/pandas/pandas/tests/io/test_fsspec.py
"""Regression test for writing to a not-yet-existent GCS Parquet file."""
df1.to_parquet(
    "memory://test/test.csv", index=True, engine="fastparquet", compression=None
)
