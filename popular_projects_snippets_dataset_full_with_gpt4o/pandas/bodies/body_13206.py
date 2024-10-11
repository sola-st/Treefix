# Extracted from ./data/repos/pandas/pandas/tests/io/test_parquet.py
# GH #23283
partition_cols = ["bool", "int"]
df = df_full
df.to_parquet(
    tmp_path,
    engine="fastparquet",
    compression=None,
    partition_on=partition_cols,
)
assert os.path.exists(tmp_path)
import fastparquet

actual_partition_cols = fastparquet.ParquetFile(str(tmp_path), False).cats
assert len(actual_partition_cols) == 2
