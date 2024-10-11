# Extracted from ./data/repos/pandas/pandas/io/parquet.py
"""
    Write a DataFrame to the parquet format.

    Parameters
    ----------
    df : DataFrame
    path : str, path object, file-like object, or None, default None
        String, path object (implementing ``os.PathLike[str]``), or file-like
        object implementing a binary ``write()`` function. If None, the result is
        returned as bytes. If a string, it will be used as Root Directory path
        when writing a partitioned dataset. The engine fastparquet does not
        accept file-like objects.

        .. versionchanged:: 1.2.0

    engine : {{'auto', 'pyarrow', 'fastparquet'}}, default 'auto'
        Parquet library to use. If 'auto', then the option
        ``io.parquet.engine`` is used. The default ``io.parquet.engine``
        behavior is to try 'pyarrow', falling back to 'fastparquet' if
        'pyarrow' is unavailable.
    compression : {{'snappy', 'gzip', 'brotli', 'lz4', 'zstd', None}},
        default 'snappy'. Name of the compression to use. Use ``None``
        for no compression. The supported compression methods actually
        depend on which engine is used. For 'pyarrow', 'snappy', 'gzip',
        'brotli', 'lz4', 'zstd' are all supported. For 'fastparquet',
        only 'gzip' and 'snappy' are supported.
    index : bool, default None
        If ``True``, include the dataframe's index(es) in the file output. If
        ``False``, they will not be written to the file.
        If ``None``, similar to ``True`` the dataframe's index(es)
        will be saved. However, instead of being saved as values,
        the RangeIndex will be stored as a range in the metadata so it
        doesn't require much space and is faster. Other indexes will
        be included as columns in the file output.
    partition_cols : str or list, optional, default None
        Column names by which to partition the dataset.
        Columns are partitioned in the order they are given.
        Must be None if path is not a string.
    {storage_options}

        .. versionadded:: 1.2.0

    kwargs
        Additional keyword arguments passed to the engine

    Returns
    -------
    bytes if no path argument is provided else None
    """
if isinstance(partition_cols, str):
    partition_cols = [partition_cols]
impl = get_engine(engine)

path_or_buf: FilePath | WriteBuffer[bytes] = io.BytesIO() if path is None else path

impl.write(
    df,
    path_or_buf,
    compression=compression,
    index=index,
    partition_cols=partition_cols,
    storage_options=storage_options,
    **kwargs,
)

if path is None:
    assert isinstance(path_or_buf, io.BytesIO)
    exit(path_or_buf.getvalue())
else:
    exit(None)
