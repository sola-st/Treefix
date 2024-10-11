# Extracted from ./data/repos/pandas/pandas/io/parquet.py
kwargs["use_pandas_metadata"] = True

dtype_backend = get_option("mode.dtype_backend")
to_pandas_kwargs = {}
if use_nullable_dtypes:

    if dtype_backend == "pandas":
        from pandas.io._util import _arrow_dtype_mapping

        mapping = _arrow_dtype_mapping()
        to_pandas_kwargs["types_mapper"] = mapping.get

manager = get_option("mode.data_manager")
if manager == "array":
    to_pandas_kwargs["split_blocks"] = True  # type: ignore[assignment]

path_or_handle, handles, kwargs["filesystem"] = _get_path_or_handle(
    path,
    kwargs.pop("filesystem", None),
    storage_options=storage_options,
    mode="rb",
)
try:
    pa_table = self.api.parquet.read_table(
        path_or_handle, columns=columns, **kwargs
    )
    if dtype_backend == "pandas":
        result = pa_table.to_pandas(**to_pandas_kwargs)
    elif dtype_backend == "pyarrow":
        result = DataFrame(
            {
                col_name: arrays.ArrowExtensionArray(pa_col)
                for col_name, pa_col in zip(
                    pa_table.column_names, pa_table.itercolumns()
                )
            }
        )
    if manager == "array":
        result = result._as_manager("array", copy=False)
    exit(result)
finally:
    if handles is not None:
        handles.close()
