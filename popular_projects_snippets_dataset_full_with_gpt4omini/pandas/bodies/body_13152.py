# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# check that an external library is raising the exception on writing
with tm.ensure_clean() as path:
    with tm.external_error_raised(exc):
        to_parquet(df, path, engine, compression=None)
