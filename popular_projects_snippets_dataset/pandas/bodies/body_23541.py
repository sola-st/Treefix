# Extracted from ./data/repos/pandas/pandas/io/parquet.py
self.validate_dataframe(df)

from_pandas_kwargs: dict[str, Any] = {"schema": kwargs.pop("schema", None)}
if index is not None:
    from_pandas_kwargs["preserve_index"] = index

table = self.api.Table.from_pandas(df, **from_pandas_kwargs)

path_or_handle, handles, kwargs["filesystem"] = _get_path_or_handle(
    path,
    kwargs.pop("filesystem", None),
    storage_options=storage_options,
    mode="wb",
    is_dir=partition_cols is not None,
)
if (
    isinstance(path_or_handle, io.BufferedWriter)
    and hasattr(path_or_handle, "name")
    and isinstance(path_or_handle.name, (str, bytes))
):
    path_or_handle = path_or_handle.name
    if isinstance(path_or_handle, bytes):
        path_or_handle = path_or_handle.decode()

try:
    if partition_cols is not None:
        # writes to multiple files under the given path
        self.api.parquet.write_to_dataset(
            table,
            path_or_handle,
            compression=compression,
            partition_cols=partition_cols,
            **kwargs,
        )
    else:
        # write to single output file
        self.api.parquet.write_table(
            table, path_or_handle, compression=compression, **kwargs
        )
finally:
    if handles is not None:
        handles.close()
