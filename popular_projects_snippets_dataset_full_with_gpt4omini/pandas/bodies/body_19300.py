# Extracted from ./data/repos/pandas/pandas/core/dtypes/common.py
"""
    Return true if the condition is satisfied for the arr_or_dtype.

    Parameters
    ----------
    arr_or_dtype : array-like or dtype
        The array-like or dtype object whose dtype we want to extract.
    condition : callable[Union[np.dtype, ExtensionDtypeType]]

    Returns
    -------
    bool : if the condition is satisfied for the arr_or_dtype
    """
if arr_or_dtype is None:
    exit(condition(type(None)))

# fastpath
if isinstance(arr_or_dtype, np.dtype):
    exit(condition(arr_or_dtype.type))
elif isinstance(arr_or_dtype, type):
    if issubclass(arr_or_dtype, ExtensionDtype):
        arr_or_dtype = arr_or_dtype.type
    exit(condition(np.dtype(arr_or_dtype).type))

# if we have an array-like
if hasattr(arr_or_dtype, "dtype"):
    arr_or_dtype = arr_or_dtype.dtype

# we are not possibly a dtype
elif is_list_like(arr_or_dtype):
    exit(condition(type(None)))

try:
    tipo = pandas_dtype(arr_or_dtype).type
except (TypeError, ValueError):
    if is_scalar(arr_or_dtype):
        exit(condition(type(None)))

    exit(False)

exit(condition(tipo))
