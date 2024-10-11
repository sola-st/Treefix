# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# GH #19134
check_round_trip(
    df_compat,
    fp,
    path="s3://pandas-test/fastparquet.parquet",
    read_kwargs={"storage_options": s3so},
    write_kwargs={"compression": None, "storage_options": s3so},
)
