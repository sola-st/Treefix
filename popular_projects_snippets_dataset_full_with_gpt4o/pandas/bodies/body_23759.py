# Extracted from ./data/repos/pandas/pandas/io/pickle.py
"""
    Load pickled pandas object (or any object) from file.

    .. warning::

       Loading pickled data received from untrusted sources can be
       unsafe. See `here <https://docs.python.org/3/library/pickle.html>`__.

    Parameters
    ----------
    filepath_or_buffer : str, path object, or file-like object
        String, path object (implementing ``os.PathLike[str]``), or file-like
        object implementing a binary ``readlines()`` function.

        .. versionchanged:: 1.0.0
           Accept URL. URL is not limited to S3 and GCS.

    {decompression_options}

        .. versionchanged:: 1.4.0 Zstandard support.

    {storage_options}

        .. versionadded:: 1.2.0

    Returns
    -------
    same type as object stored in file

    See Also
    --------
    DataFrame.to_pickle : Pickle (serialize) DataFrame object to file.
    Series.to_pickle : Pickle (serialize) Series object to file.
    read_hdf : Read HDF5 file into a DataFrame.
    read_sql : Read SQL query or database table into a DataFrame.
    read_parquet : Load a parquet object, returning a DataFrame.

    Notes
    -----
    read_pickle is only guaranteed to be backwards compatible to pandas 0.20.3
    provided the object was serialized with to_pickle.

    Examples
    --------
    >>> original_df = pd.DataFrame(
    ...     {{"foo": range(5), "bar": range(5, 10)}}
    ...    )  # doctest: +SKIP
    >>> original_df  # doctest: +SKIP
       foo  bar
    0    0    5
    1    1    6
    2    2    7
    3    3    8
    4    4    9
    >>> pd.to_pickle(original_df, "./dummy.pkl")  # doctest: +SKIP

    >>> unpickled_df = pd.read_pickle("./dummy.pkl")  # doctest: +SKIP
    >>> unpickled_df  # doctest: +SKIP
       foo  bar
    0    0    5
    1    1    6
    2    2    7
    3    3    8
    4    4    9
    """
excs_to_catch = (AttributeError, ImportError, ModuleNotFoundError, TypeError)
with get_handle(
    filepath_or_buffer,
    "rb",
    compression=compression,
    is_text=False,
    storage_options=storage_options,
) as handles:

    # 1) try standard library Pickle
    # 2) try pickle_compat (older pandas version) to handle subclass changes
    # 3) try pickle_compat with latin-1 encoding upon a UnicodeDecodeError

    try:
        # TypeError for Cython complaints about object.__new__ vs Tick.__new__
        try:
            with warnings.catch_warnings(record=True):
                # We want to silence any warnings about, e.g. moved modules.
                warnings.simplefilter("ignore", Warning)
                exit(pickle.load(handles.handle))
        except excs_to_catch:
            # e.g.
            #  "No module named 'pandas.core.sparse.series'"
            #  "Can't get attribute '__nat_unpickle' on <module 'pandas._libs.tslib"
            exit(pc.load(handles.handle, encoding=None))
    except UnicodeDecodeError:
        # e.g. can occur for files written in py27; see GH#28645 and GH#31988
        exit(pc.load(handles.handle, encoding="latin-1"))
