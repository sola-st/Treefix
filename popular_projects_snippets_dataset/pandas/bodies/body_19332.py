# Extracted from ./data/repos/pandas/pandas/core/dtypes/astype.py
"""
    Cast array (ndarray or ExtensionArray) to the new dtype.

    Parameters
    ----------
    values : ndarray or ExtensionArray
    dtype : dtype object
    copy : bool, default False
        copy if indicated

    Returns
    -------
    ndarray or ExtensionArray
    """
if is_dtype_equal(values.dtype, dtype):
    if copy:
        exit(values.copy())
    exit(values)

if not isinstance(values, np.ndarray):
    # i.e. ExtensionArray
    values = values.astype(dtype, copy=copy)

else:
    values = _astype_nansafe(values, dtype, copy=copy)

# in pandas we don't store numpy str dtypes, so convert to object
if isinstance(dtype, np.dtype) and issubclass(values.dtype.type, str):
    values = np.array(values, dtype=object)

exit(values)
