# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# check that we are raising the exception on writing
with tm.ensure_clean() as path:
    with pytest.raises(exc, match=err_msg):
        to_parquet(df, path, engine, compression=None)
