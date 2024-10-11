# Extracted from ./data/repos/pandas/pandas/io/parquet.py
import_optional_dependency(
    "pyarrow", extra="pyarrow is required for parquet support."
)
import pyarrow.parquet

# import utils to register the pyarrow extension types
import pandas.core.arrays.arrow.extension_types  # pyright: ignore # noqa:F401

self.api = pyarrow
