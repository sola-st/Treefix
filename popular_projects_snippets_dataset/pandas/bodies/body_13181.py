# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# GH #26388
expected_df = df_compat.copy()

# GH #35791
if partition_col:
    expected_df = expected_df.astype(dict.fromkeys(partition_col, np.int32))
    partition_col_type = "category"

    expected_df[partition_col] = expected_df[partition_col].astype(
        partition_col_type
    )

check_round_trip(
    df_compat,
    pa,
    expected=expected_df,
    path="s3://pandas-test/parquet_dir",
    read_kwargs={"storage_options": s3so},
    write_kwargs={
        "partition_cols": partition_col,
        "compression": None,
        "storage_options": s3so,
    },
    check_like=True,
    repeat=1,
)
