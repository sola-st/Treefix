# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
s3fs = pytest.importorskip("s3fs")
s3 = s3fs.S3FileSystem(**s3so)
kw = {"filesystem": s3}
check_round_trip(
    df_compat,
    pa,
    path="pandas-test/pyarrow.parquet",
    read_kwargs=kw,
    write_kwargs=kw,
)
