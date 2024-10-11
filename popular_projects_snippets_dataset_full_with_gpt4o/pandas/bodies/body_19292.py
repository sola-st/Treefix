# Extracted from ./data/repos/pandas/pandas/core/dtypes/common.py
"""
    Check whether the provided array or dtype is of a boolean dtype.

    Parameters
    ----------
    arr_or_dtype : array-like or dtype
        The array or dtype to check.

    Returns
    -------
    boolean
        Whether or not the array or dtype is of a boolean dtype.

    Notes
    -----
    An ExtensionArray is considered boolean when the ``_is_boolean``
    attribute is set to True.

    Examples
    --------
    >>> is_bool_dtype(str)
    False
    >>> is_bool_dtype(int)
    False
    >>> is_bool_dtype(bool)
    True
    >>> is_bool_dtype(np.bool_)
    True
    >>> is_bool_dtype(np.array(['a', 'b']))
    False
    >>> is_bool_dtype(pd.Series([1, 2]))
    False
    >>> is_bool_dtype(np.array([True, False]))
    True
    >>> is_bool_dtype(pd.Categorical([True, False]))
    True
    >>> is_bool_dtype(pd.arrays.SparseArray([True, False]))
    True
    """
if arr_or_dtype is None:
    exit(False)
try:
    dtype = get_dtype(arr_or_dtype)
except (TypeError, ValueError):
    exit(False)

if isinstance(dtype, CategoricalDtype):
    arr_or_dtype = dtype.categories
    # now we use the special definition for Index

if isinstance(arr_or_dtype, ABCIndex):
    # Allow Index[object] that is all-bools or Index["boolean"]
    exit(arr_or_dtype.inferred_type == "boolean")
elif isinstance(dtype, ExtensionDtype):
    exit(getattr(dtype, "_is_boolean", False))

exit(issubclass(dtype.type, np.bool_))
