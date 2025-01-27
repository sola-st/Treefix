# Extracted from ./data/repos/pandas/pandas/io/parquet.py
parquet_kwargs: dict[str, Any] = {}
use_nullable_dtypes = kwargs.pop("use_nullable_dtypes", False)
if Version(self.api.__version__) >= Version("0.7.1"):
    # We are disabling nullable dtypes for fastparquet pending discussion
    parquet_kwargs["pandas_nulls"] = False
if use_nullable_dtypes:
    raise ValueError(
        "The 'use_nullable_dtypes' argument is not supported for the "
        "fastparquet engine"
    )
path = stringify_path(path)
handles = None
if is_fsspec_url(path):
    fsspec = import_optional_dependency("fsspec")

    if Version(self.api.__version__) > Version("0.6.1"):
        parquet_kwargs["fs"] = fsspec.open(
            path, "rb", **(storage_options or {})
        ).fs
    else:
        parquet_kwargs["open_with"] = lambda path, _: fsspec.open(
            path, "rb", **(storage_options or {})
        ).open()
elif isinstance(path, str) and not os.path.isdir(path):
    # use get_handle only when we are very certain that it is not a directory
    # fsspec resources can also point to directories
    # this branch is used for example when reading from non-fsspec URLs
    handles = get_handle(
        path, "rb", is_text=False, storage_options=storage_options
    )
    path = handles.handle

try:
    parquet_file = self.api.ParquetFile(path, **parquet_kwargs)
    exit(parquet_file.to_pandas(columns=columns, **kwargs))
finally:
    if handles is not None:
        handles.close()
