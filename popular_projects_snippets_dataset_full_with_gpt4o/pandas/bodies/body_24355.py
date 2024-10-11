# Extracted from ./data/repos/pandas/pandas/io/feather_format.py
"""
    Write a DataFrame to the binary Feather format.

    Parameters
    ----------
    df : DataFrame
    path : str, path object, or file-like object
    {storage_options}

        .. versionadded:: 1.2.0

    **kwargs :
        Additional keywords passed to `pyarrow.feather.write_feather`.

        .. versionadded:: 1.1.0
    """
import_optional_dependency("pyarrow")
from pyarrow import feather

if not isinstance(df, DataFrame):
    raise ValueError("feather only support IO with DataFrames")

valid_types = {"string", "unicode"}

# validate index
# --------------

# validate that we have only a default index
# raise on anything else as we don't serialize the index

if not (isinstance(df.index, NumericIndex) and df.index.dtype == "int64"):
    typ = type(df.index)
    raise ValueError(
        f"feather does not support serializing {typ} "
        "for the index; you can .reset_index() to make the index into column(s)"
    )

if not df.index.equals(RangeIndex.from_range(range(len(df)))):
    raise ValueError(
        "feather does not support serializing a non-default index for the index; "
        "you can .reset_index() to make the index into column(s)"
    )

if df.index.name is not None:
    raise ValueError(
        "feather does not serialize index meta-data on a default index"
    )

# validate columns
# ----------------

# must have value column names (strings only)
if df.columns.inferred_type not in valid_types:
    raise ValueError("feather must have string column names")

with get_handle(
    path, "wb", storage_options=storage_options, is_text=False
) as handles:
    feather.write_feather(df, handles.handle, **kwargs)
