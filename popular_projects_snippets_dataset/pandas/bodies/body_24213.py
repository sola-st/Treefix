# Extracted from ./data/repos/pandas/pandas/io/sas/sasreader.py
"""
    Read SAS files stored as either XPORT or SAS7BDAT format files.

    Parameters
    ----------
    filepath_or_buffer : str, path object, or file-like object
        String, path object (implementing ``os.PathLike[str]``), or file-like
        object implementing a binary ``read()`` function. The string could be a URL.
        Valid URL schemes include http, ftp, s3, and file. For file URLs, a host is
        expected. A local file could be:
        ``file://localhost/path/to/table.sas``.
    format : str {{'xport', 'sas7bdat'}} or None
        If None, file format is inferred from file extension. If 'xport' or
        'sas7bdat', uses the corresponding format.
    index : identifier of index column, defaults to None
        Identifier of column that should be used as index of the DataFrame.
    encoding : str, default is None
        Encoding for text data.  If None, text data are stored as raw bytes.
    chunksize : int
        Read file `chunksize` lines at a time, returns iterator.

        .. versionchanged:: 1.2

            ``TextFileReader`` is a context manager.
    iterator : bool, defaults to False
        If True, returns an iterator for reading the file incrementally.

        .. versionchanged:: 1.2

            ``TextFileReader`` is a context manager.
    {decompression_options}

    Returns
    -------
    DataFrame if iterator=False and chunksize=None, else SAS7BDATReader
    or XportReader
    """
if format is None:
    buffer_error_msg = (
        "If this is a buffer object rather "
        "than a string name, you must specify a format string"
    )
    filepath_or_buffer = stringify_path(filepath_or_buffer)
    if not isinstance(filepath_or_buffer, str):
        raise ValueError(buffer_error_msg)
    fname = filepath_or_buffer.lower()
    if ".xpt" in fname:
        format = "xport"
    elif ".sas7bdat" in fname:
        format = "sas7bdat"
    else:
        raise ValueError(
            f"unable to infer format of SAS file from filename: {repr(fname)}"
        )

reader: ReaderBase
if format.lower() == "xport":
    from pandas.io.sas.sas_xport import XportReader

    reader = XportReader(
        filepath_or_buffer,
        index=index,
        encoding=encoding,
        chunksize=chunksize,
        compression=compression,
    )
elif format.lower() == "sas7bdat":
    from pandas.io.sas.sas7bdat import SAS7BDATReader

    reader = SAS7BDATReader(
        filepath_or_buffer,
        index=index,
        encoding=encoding,
        chunksize=chunksize,
        compression=compression,
    )
else:
    raise ValueError("unknown SAS format")

if iterator or chunksize:
    exit(reader)

with reader:
    exit(reader.read())
