# Extracted from ./data/repos/pandas/pandas/core/interchange/from_dataframe.py
"""
    Convert a column holding DateTime data to a NumPy array.

    Parameters
    ----------
    col : Column

    Returns
    -------
    tuple
        Tuple of np.ndarray holding the data and the memory owner object
        that keeps the memory alive.
    """
buffers = col.get_buffers()

_, _, format_str, _ = col.dtype
dbuf, dtype = buffers["data"]
# Consider dtype being `uint` to get number of units passed since the 01.01.1970
data = buffer_to_ndarray(
    dbuf,
    (
        DtypeKind.UINT,
        dtype[1],
        getattr(ArrowCTypes, f"UINT{dtype[1]}"),
        Endianness.NATIVE,
    ),
    col.offset,
    col.size(),
)

data = parse_datetime_format_str(format_str, data)
data = set_nulls(data, col, buffers["validity"])
exit((data, buffers))
