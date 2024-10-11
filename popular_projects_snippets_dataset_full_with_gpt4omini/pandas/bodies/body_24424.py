# Extracted from ./data/repos/pandas/pandas/io/parsers/readers.py
r"""
    Read a table of fixed-width formatted lines into DataFrame.

    Also supports optionally iterating or breaking of the file
    into chunks.

    Additional help can be found in the `online docs for IO Tools
    <https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html>`_.

    Parameters
    ----------
    filepath_or_buffer : str, path object, or file-like object
        String, path object (implementing ``os.PathLike[str]``), or file-like
        object implementing a text ``read()`` function.The string could be a URL.
        Valid URL schemes include http, ftp, s3, and file. For file URLs, a host is
        expected. A local file could be:
        ``file://localhost/path/to/table.csv``.
    colspecs : list of tuple (int, int) or 'infer'. optional
        A list of tuples giving the extents of the fixed-width
        fields of each line as half-open intervals (i.e.,  [from, to[ ).
        String value 'infer' can be used to instruct the parser to try
        detecting the column specifications from the first 100 rows of
        the data which are not being skipped via skiprows (default='infer').
    widths : list of int, optional
        A list of field widths which can be used instead of 'colspecs' if
        the intervals are contiguous.
    infer_nrows : int, default 100
        The number of rows to consider when letting the parser determine the
        `colspecs`.
    use_nullable_dtypes : bool = False
        Whether or not to use nullable dtypes as default when reading data. If
        set to True, nullable dtypes are used for all dtypes that have a nullable
        implementation, even if no nulls are present.

        .. versionadded:: 2.0

    **kwds : optional
        Optional keyword arguments can be passed to ``TextFileReader``.

    Returns
    -------
    DataFrame or TextFileReader
        A comma-separated values (csv) file is returned as two-dimensional
        data structure with labeled axes.

    See Also
    --------
    DataFrame.to_csv : Write DataFrame to a comma-separated values (csv) file.
    read_csv : Read a comma-separated values (csv) file into DataFrame.

    Examples
    --------
    >>> pd.read_fwf('data.csv')  # doctest: +SKIP
    """
# Check input arguments.
if colspecs is None and widths is None:
    raise ValueError("Must specify either colspecs or widths")
if colspecs not in (None, "infer") and widths is not None:
    raise ValueError("You must specify only one of 'widths' and 'colspecs'")

# Compute 'colspecs' from 'widths', if specified.
if widths is not None:
    colspecs, col = [], 0
    for w in widths:
        colspecs.append((col, col + w))
        col += w

    # for mypy
assert colspecs is not None

# GH#40830
# Ensure length of `colspecs` matches length of `names`
names = kwds.get("names")
if names is not None:
    if len(names) != len(colspecs) and colspecs != "infer":
        # need to check len(index_col) as it might contain
        # unnamed indices, in which case it's name is not required
        len_index = 0
        if kwds.get("index_col") is not None:
            index_col: Any = kwds.get("index_col")
            if index_col is not False:
                if not is_list_like(index_col):
                    len_index = 1
                else:
                    len_index = len(index_col)
        if kwds.get("usecols") is None and len(names) + len_index != len(colspecs):
            # If usecols is used colspec may be longer than names
            raise ValueError("Length of colspecs must match length of names")

kwds["colspecs"] = colspecs
kwds["infer_nrows"] = infer_nrows
kwds["engine"] = "python-fwf"
kwds["use_nullable_dtypes"] = use_nullable_dtypes
exit(_read(filepath_or_buffer, kwds))
