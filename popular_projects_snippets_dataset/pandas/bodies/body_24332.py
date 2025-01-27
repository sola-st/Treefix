# Extracted from ./data/repos/pandas/pandas/io/orc.py
"""
    Load an ORC object from the file path, returning a DataFrame.

    .. versionadded:: 1.0.0

    Parameters
    ----------
    path : str, path object, or file-like object
        String, path object (implementing ``os.PathLike[str]``), or file-like
        object implementing a binary ``read()`` function. The string could be a URL.
        Valid URL schemes include http, ftp, s3, and file. For file URLs, a host is
        expected. A local file could be:
        ``file://localhost/path/to/table.orc``.
    columns : list, default None
        If not None, only these columns will be read from the file.
        Output always follows the ordering of the file and not the columns list.
        This mirrors the original behaviour of
        :external+pyarrow:py:meth:`pyarrow.orc.ORCFile.read`.
    use_nullable_dtypes : bool, default False
        If True, use dtypes that use ``pd.NA`` as missing value indicator
        for the resulting DataFrame.

        The nullable dtype implementation can be configured by calling
        ``pd.set_option("mode.dtype_backend", "pandas")`` to use
        numpy-backed nullable dtypes or
        ``pd.set_option("mode.dtype_backend", "pyarrow")`` to use
        pyarrow-backed nullable dtypes (using ``pd.ArrowDtype``).

        .. versionadded:: 2.0.0

        .. note

            Currently only ``mode.dtype_backend`` set to ``"pyarrow"`` is supported.

    **kwargs
        Any additional kwargs are passed to pyarrow.

    Returns
    -------
    DataFrame

    Notes
    -----
    Before using this function you should read the :ref:`user guide about ORC <io.orc>`
    and :ref:`install optional dependencies <install.warn_orc>`.
    """
# we require a newer version of pyarrow than we support for parquet

orc = import_optional_dependency("pyarrow.orc")

with get_handle(path, "rb", is_text=False) as handles:
    orc_file = orc.ORCFile(handles.handle)
    pa_table = orc_file.read(columns=columns, **kwargs)
if use_nullable_dtypes:
    dtype_backend = get_option("mode.dtype_backend")
    if dtype_backend == "pyarrow":
        df = DataFrame(
            {
                col_name: ArrowExtensionArray(pa_col)
                for col_name, pa_col in zip(
                    pa_table.column_names, pa_table.itercolumns()
                )
            }
        )
    else:
        from pandas.io._util import _arrow_dtype_mapping

        mapping = _arrow_dtype_mapping()
        df = pa_table.to_pandas(types_mapper=mapping.get)
    exit(df)
else:
    exit(pa_table.to_pandas())
