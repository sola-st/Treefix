# Extracted from ./data/repos/pandas/pandas/io/parquet.py
self.validate_dataframe(df)

if "partition_on" in kwargs and partition_cols is not None:
    raise ValueError(
        "Cannot use both partition_on and "
        "partition_cols. Use partition_cols for partitioning data"
    )
if "partition_on" in kwargs:
    partition_cols = kwargs.pop("partition_on")

if partition_cols is not None:
    kwargs["file_scheme"] = "hive"

# cannot use get_handle as write() does not accept file buffers
path = stringify_path(path)
if is_fsspec_url(path):
    fsspec = import_optional_dependency("fsspec")

    # if filesystem is provided by fsspec, file must be opened in 'wb' mode.
    kwargs["open_with"] = lambda path, _: fsspec.open(
        path, "wb", **(storage_options or {})
    ).open()
elif storage_options:
    raise ValueError(
        "storage_options passed with file object or non-fsspec file path"
    )

with catch_warnings(record=True):
    self.api.write(
        path,
        df,
        compression=compression,
        write_index=index,
        partition_on=partition_cols,
        **kwargs,
    )
