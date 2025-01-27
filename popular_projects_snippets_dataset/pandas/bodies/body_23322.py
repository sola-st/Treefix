# Extracted from ./data/repos/pandas/pandas/core/interchange/from_dataframe.py
"""
    Convert a column holding one of the primitive dtypes to a NumPy array.

    A primitive type is one of: int, uint, float, bool.

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

data_buff, data_dtype = buffers["data"]
data = buffer_to_ndarray(data_buff, data_dtype, col.offset, col.size())

data = set_nulls(data, col, buffers["validity"])
exit((data, buffers))
