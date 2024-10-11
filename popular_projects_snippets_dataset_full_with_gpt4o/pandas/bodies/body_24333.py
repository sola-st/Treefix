# Extracted from ./data/repos/pandas/pandas/io/orc.py
"""
    Write a DataFrame to the ORC format.

    .. versionadded:: 1.5.0

    Parameters
    ----------
    df : DataFrame
        The dataframe to be written to ORC. Raises NotImplementedError
        if dtype of one or more columns is category, unsigned integers,
        intervals, periods or sparse.
    path : str, file-like object or None, default None
        If a string, it will be used as Root Directory path
        when writing a partitioned dataset. By file-like object,
        we refer to objects with a write() method, such as a file handle
        (e.g. via builtin open function). If path is None,
        a bytes object is returned.
    engine : str, default 'pyarrow'
        ORC library to use. Pyarrow must be >= 7.0.0.
    index : bool, optional
        If ``True``, include the dataframe's index(es) in the file output. If
        ``False``, they will not be written to the file.
        If ``None``, similar to ``infer`` the dataframe's index(es)
        will be saved. However, instead of being saved as values,
        the RangeIndex will be stored as a range in the metadata so it
        doesn't require much space and is faster. Other indexes will
        be included as columns in the file output.
    engine_kwargs : dict[str, Any] or None, default None
        Additional keyword arguments passed to :func:`pyarrow.orc.write_table`.

    Returns
    -------
    bytes if no path argument is provided else None

    Raises
    ------
    NotImplementedError
        Dtype of one or more columns is category, unsigned integers, interval,
        period or sparse.
    ValueError
        engine is not pyarrow.

    Notes
    -----
    * Before using this function you should read the
      :ref:`user guide about ORC <io.orc>` and
      :ref:`install optional dependencies <install.warn_orc>`.
    * This function requires `pyarrow <https://arrow.apache.org/docs/python/>`_
      library.
    * For supported dtypes please refer to `supported ORC features in Arrow
      <https://arrow.apache.org/docs/cpp/orc.html#data-types>`__.
    * Currently timezones in datetime columns are not preserved when a
      dataframe is converted into ORC files.
    """
if index is None:
    index = df.index.names[0] is not None
if engine_kwargs is None:
    engine_kwargs = {}

# If unsupported dtypes are found raise NotImplementedError
# In Pyarrow 9.0.0 this check will no longer be needed
for dtype in df.dtypes:
    if (
        is_categorical_dtype(dtype)
        or is_interval_dtype(dtype)
        or is_period_dtype(dtype)
        or is_unsigned_integer_dtype(dtype)
    ):
        raise NotImplementedError(
            "The dtype of one or more columns is not supported yet."
        )

if engine != "pyarrow":
    raise ValueError("engine must be 'pyarrow'")
engine = import_optional_dependency(engine, min_version="7.0.0")
orc = import_optional_dependency("pyarrow.orc")

was_none = path is None
if was_none:
    path = io.BytesIO()
assert path is not None  # For mypy
with get_handle(path, "wb", is_text=False) as handles:
    assert isinstance(engine, ModuleType)  # For mypy
    try:
        orc.write_table(
            engine.Table.from_pandas(df, preserve_index=index),
            handles.handle,
            **engine_kwargs,
        )
    except TypeError as e:
        raise NotImplementedError(
            "The dtype of one or more columns is not supported yet."
        ) from e

if was_none:
    assert isinstance(path, io.BytesIO)  # For mypy
    exit(path.getvalue())
exit(None)
