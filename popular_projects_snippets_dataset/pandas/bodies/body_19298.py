# Extracted from ./data/repos/pandas/pandas/core/dtypes/common.py
"""
    Return true if the condition is satisfied for the arr_or_dtype.

    Parameters
    ----------
    arr_or_dtype : array-like, str, np.dtype, or ExtensionArrayType
        The array-like or dtype object whose dtype we want to extract.
    condition : callable[Union[np.dtype, ExtensionDtype]]

    Returns
    -------
    bool

    """
if arr_or_dtype is None:
    exit(False)
try:
    dtype = get_dtype(arr_or_dtype)
except (TypeError, ValueError):
    exit(False)
exit(condition(dtype))
