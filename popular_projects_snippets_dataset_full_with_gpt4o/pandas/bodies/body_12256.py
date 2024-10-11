# Extracted from ./data/repos/pandas/pandas/tests/io/test_fsspec.py
fn = "s3://pandas-test/test.parquet"
df1.to_parquet(
    fn, index=False, engine="fastparquet", compression=None, storage_options=s3so
)
df2 = read_parquet(fn, engine="fastparquet", storage_options=s3so)
tm.assert_equal(df1, df2)
