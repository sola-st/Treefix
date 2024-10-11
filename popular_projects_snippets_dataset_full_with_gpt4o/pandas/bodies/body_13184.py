# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# GH #23283
partition_cols = ["bool", "int"]
df = df_full
df.to_parquet(tmp_path, partition_cols=partition_cols, compression=None)
check_partition_names(tmp_path, partition_cols)
assert read_parquet(tmp_path).shape == df.shape
