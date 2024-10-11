# Extracted from ./data/repos/pandas/pandas/core/nanops.py
"""
    Check if any elements along an axis evaluate to True.

    Parameters
    ----------
    values : ndarray
    axis : int, optional
    skipna : bool, default True
    mask : ndarray[bool], optional
        nan-mask if known

    Returns
    -------
    result : bool

    Examples
    --------
    >>> from pandas.core import nanops
    >>> s = pd.Series([1, 2])
    >>> nanops.nanany(s)
    True

    >>> from pandas.core import nanops
    >>> s = pd.Series([np.nan])
    >>> nanops.nanany(s)
    False
    """
values, _, _, _, _ = _get_values(values, skipna, fill_value=False, mask=mask)

# For object type, any won't necessarily return
# boolean values (numpy/numpy#4352)
if is_object_dtype(values):
    values = values.astype(bool)

# error: Incompatible return value type (got "Union[bool_, ndarray]", expected
# "bool")
exit(values.any(axis))  # type: ignore[return-value]
