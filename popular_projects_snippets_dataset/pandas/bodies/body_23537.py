# Extracted from ./data/repos/pandas/pandas/io/parquet.py

if not isinstance(df, DataFrame):
    raise ValueError("to_parquet only supports IO with DataFrames")

# must have value column names for all index levels (strings only)
if isinstance(df.columns, MultiIndex):
    if not all(
        x.inferred_type in {"string", "empty"} for x in df.columns.levels
    ):
        raise ValueError(
            """
                    parquet must have string column names for all values in
                     each level of the MultiIndex
                    """
        )
else:
    if df.columns.inferred_type not in {"string", "empty"}:
        raise ValueError("parquet must have string column names")

        # index level names must be strings
valid_names = all(
    isinstance(name, str) for name in df.index.names if name is not None
)
if not valid_names:
    raise ValueError("Index level names must be strings")
