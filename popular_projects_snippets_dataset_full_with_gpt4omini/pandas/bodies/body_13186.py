# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# GH 35902

partition_cols = "B"
partition_cols_list = [partition_cols]
df = df_compat

path = path_type(tmp_path)
df.to_parquet(path, partition_cols=partition_cols_list)
assert read_parquet(path).shape == df.shape
