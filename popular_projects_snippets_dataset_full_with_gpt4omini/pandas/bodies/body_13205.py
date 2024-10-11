# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# GH #27117
partition_cols = "bool"
df = df_full
df.to_parquet(
    tmp_path,
    engine="fastparquet",
    partition_cols=partition_cols,
    compression=None,
)
assert os.path.exists(tmp_path)
import fastparquet

actual_partition_cols = fastparquet.ParquetFile(str(tmp_path), False).cats
assert len(actual_partition_cols) == 1
