# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# GH #23283
partition_cols = ["bool", "int"]
df = df_full
msg = (
    "Cannot use both partition_on and partition_cols. Use partition_cols for "
    "partitioning data"
)
with pytest.raises(ValueError, match=msg):
    df.to_parquet(
        tmp_path,
        engine="fastparquet",
        compression=None,
        partition_on=partition_cols,
        partition_cols=partition_cols,
    )
