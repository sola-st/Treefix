# Extracted from ./data/repos/pandas/pandas/io/feather_format.py
"""
    Load a feather-format object from the file path.

    Parameters
    ----------
    path : str, path object, or file-like object
        String, path object (implementing ``os.PathLike[str]``), or file-like
        object implementing a binary ``read()`` function. The string could be a URL.
        Valid URL schemes include http, ftp, s3, and file. For file URLs, a host is
        expected. A local file could be: ``file://localhost/path/to/table.feather``.
    columns : sequence, default None
        If not provided, all columns are read.
    use_threads : bool, default True
        Whether to parallelize reading using multiple threads.
    {storage_options}

        .. versionadded:: 1.2.0

    use_nullable_dtypes : bool = False
        Whether or not to use nullable dtypes as default when reading data. If
        set to True, nullable dtypes are used for all dtypes that have a nullable
        implementation, even if no nulls are present.

        The nullable dtype implementation can be configured by calling
        ``pd.set_option("mode.dtype_backend", "pandas")`` to use
        numpy-backed nullable dtypes or
        ``pd.set_option("mode.dtype_backend", "pyarrow")`` to use
        pyarrow-backed nullable dtypes (using ``pd.ArrowDtype``).

        .. versionadded:: 2.0

    Returns
    -------
    type of object stored in file
    """
import_optional_dependency("pyarrow")
from pyarrow import feather

with get_handle(
    path, "rb", storage_options=storage_options, is_text=False
) as handles:
    if not use_nullable_dtypes:
        exit(feather.read_feather(
            handles.handle, columns=columns, use_threads=bool(use_threads)
        ))

    dtype_backend = get_option("mode.dtype_backend")

    pa_table = feather.read_table(
        handles.handle, columns=columns, use_threads=bool(use_threads)
    )

    if dtype_backend == "pandas":
        from pandas.io._util import _arrow_dtype_mapping

        exit(pa_table.to_pandas(types_mapper=_arrow_dtype_mapping().get))

    elif dtype_backend == "pyarrow":
        exit(DataFrame(
            {
                col_name: arrays.ArrowExtensionArray(pa_col)
                for col_name, pa_col in zip(
                    pa_table.column_names, pa_table.itercolumns()
                )
            }
        ))
