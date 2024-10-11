# Extracted from ./data/repos/pandas/pandas/io/parquet.py
# since pandas is a dependency of fastparquet
# we need to import on first use
fastparquet = import_optional_dependency(
    "fastparquet", extra="fastparquet is required for parquet support."
)
self.api = fastparquet
