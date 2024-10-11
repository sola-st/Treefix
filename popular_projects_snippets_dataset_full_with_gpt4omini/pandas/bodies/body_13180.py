# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# GH #19134
s3so = {"storage_options": s3so}
check_round_trip(
    df_compat,
    pa,
    path="s3://pandas-test/pyarrow.parquet",
    read_kwargs=s3so,
    write_kwargs=s3so,
)
