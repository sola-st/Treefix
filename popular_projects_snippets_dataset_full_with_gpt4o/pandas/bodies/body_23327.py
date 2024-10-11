# Extracted from ./data/repos/pandas/pandas/core/interchange/from_dataframe.py
"""
    Build a NumPy array from the passed buffer.

    Parameters
    ----------
    buffer : Buffer
        Buffer to build a NumPy array from.
    dtype : tuple
        Data type of the buffer conforming protocol dtypes format.
    offset : int, default: 0
        Number of elements to offset from the start of the buffer.
    length : int, optional
        If the buffer is a bit-mask, specifies a number of bits to read
        from the buffer. Has no effect otherwise.

    Returns
    -------
    np.ndarray

    Notes
    -----
    The returned array doesn't own the memory. The caller of this function is
    responsible for keeping the memory owner object alive as long as
    the returned NumPy array is being used.
    """
kind, bit_width, _, _ = dtype

column_dtype = _NP_DTYPES.get(kind, {}).get(bit_width, None)
if column_dtype is None:
    raise NotImplementedError(f"Conversion for {dtype} is not yet supported.")

# TODO: No DLPack yet, so need to construct a new ndarray from the data pointer
# and size in the buffer plus the dtype on the column. Use DLPack as NumPy supports
# it since https://github.com/numpy/numpy/pull/19083
ctypes_type = np.ctypeslib.as_ctypes_type(column_dtype)
data_pointer = ctypes.cast(
    buffer.ptr + (offset * bit_width // 8), ctypes.POINTER(ctypes_type)
)

if bit_width == 1:
    assert length is not None, "`length` must be specified for a bit-mask buffer."
    arr = np.ctypeslib.as_array(data_pointer, shape=(buffer.bufsize,))
    exit(bitmask_to_bool_ndarray(arr, length, first_byte_offset=offset % 8))
else:
    exit(np.ctypeslib.as_array(
        data_pointer, shape=(buffer.bufsize // (bit_width // 8),)
    ))
