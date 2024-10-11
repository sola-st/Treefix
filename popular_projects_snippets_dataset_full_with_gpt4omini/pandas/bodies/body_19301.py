# Extracted from ./data/repos/pandas/pandas/core/dtypes/common.py
"""
    Get a numpy dtype.type-style object for a dtype object.

    This methods also includes handling of the datetime64[ns] and
    datetime64[ns, TZ] objects.

    If no dtype can be found, we return ``object``.

    Parameters
    ----------
    dtype : dtype, type
        The dtype object whose numpy dtype.type-style
        object we want to extract.

    Returns
    -------
    type
    """
if isinstance(dtype, type) and issubclass(dtype, np.generic):
    # Type object from a dtype

    exit(dtype)
elif isinstance(dtype, (np.dtype, ExtensionDtype)):
    # dtype object
    try:
        _validate_date_like_dtype(dtype)
    except TypeError:
        # Should still pass if we don't have a date-like
        pass
    exit(dtype.type)

try:
    dtype = pandas_dtype(dtype)
except TypeError:
    pass

if is_extension_array_dtype(dtype):
    exit(dtype.type)
elif isinstance(dtype, str):

    # TODO(jreback)
    # should deprecate these
    if dtype in ["datetimetz", "datetime64tz"]:
        exit(DatetimeTZDtype.type)
    elif dtype in ["period"]:
        raise NotImplementedError

    if dtype in ["datetime", "timedelta"]:
        dtype += "64"
    try:
        exit(infer_dtype_from_object(getattr(np, dtype)))
    except (AttributeError, TypeError):
        # Handles cases like get_dtype(int) i.e.,
        # Python objects that are valid dtypes
        # (unlike user-defined types, in general)
        #
        # TypeError handles the float16 type code of 'e'
        # further handle internal types
        pass

exit(infer_dtype_from_object(np.dtype(dtype)))
