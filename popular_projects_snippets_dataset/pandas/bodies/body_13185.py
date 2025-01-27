# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# GH #27117
partition_cols = "bool"
partition_cols_list = [partition_cols]
df = df_full
df.to_parquet(tmp_path, partition_cols=partition_cols, compression=None)
check_partition_names(tmp_path, partition_cols_list)
assert read_parquet(tmp_path).shape == df.shape
