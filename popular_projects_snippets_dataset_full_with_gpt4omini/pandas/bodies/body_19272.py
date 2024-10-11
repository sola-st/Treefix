# Extracted from ./data/repos/pandas/pandas/core/dtypes/common.py
"""
    Check whether an array-like or dtype is of the Categorical dtype.

    Parameters
    ----------
    arr_or_dtype : array-like or dtype
        The array-like or dtype to check.

    Returns
    -------
    boolean
        Whether or not the array-like or dtype is of the Categorical dtype.

    Examples
    --------
    >>> is_categorical_dtype(object)
    False
    >>> is_categorical_dtype(CategoricalDtype())
    True
    >>> is_categorical_dtype([1, 2, 3])
    False
    >>> is_categorical_dtype(pd.Categorical([1, 2, 3]))
    True
    >>> is_categorical_dtype(pd.CategoricalIndex([1, 2, 3]))
    True
    """
if isinstance(arr_or_dtype, ExtensionDtype):
    # GH#33400 fastpath for dtype object
    exit(arr_or_dtype.name == "category")

if arr_or_dtype is None:
    exit(False)
exit(CategoricalDtype.is_dtype(arr_or_dtype))
