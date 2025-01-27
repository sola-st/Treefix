# Extracted from ./data/repos/pandas/pandas/core/construction.py
"""
    Extract the ndarray or ExtensionArray from a Series or Index.

    For all other types, `obj` is just returned as is.

    Parameters
    ----------
    obj : object
        For Series / Index, the underlying ExtensionArray is unboxed.

    extract_numpy : bool, default False
        Whether to extract the ndarray from a PandasArray.

    extract_range : bool, default False
        If we have a RangeIndex, return range._values if True
        (which is a materialized integer ndarray), otherwise return unchanged.

    Returns
    -------
    arr : object

    Examples
    --------
    >>> extract_array(pd.Series(['a', 'b', 'c'], dtype='category'))
    ['a', 'b', 'c']
    Categories (3, object): ['a', 'b', 'c']

    Other objects like lists, arrays, and DataFrames are just passed through.

    >>> extract_array([1, 2, 3])
    [1, 2, 3]

    For an ndarray-backed Series / Index the ndarray is returned.

    >>> extract_array(pd.Series([1, 2, 3]))
    array([1, 2, 3])

    To extract all the way down to the ndarray, pass ``extract_numpy=True``.

    >>> extract_array(pd.Series([1, 2, 3]), extract_numpy=True)
    array([1, 2, 3])
    """
if isinstance(obj, (ABCIndex, ABCSeries)):
    if isinstance(obj, ABCRangeIndex):
        if extract_range:
            exit(obj._values)
        # https://github.com/python/mypy/issues/1081
        # error: Incompatible return value type (got "RangeIndex", expected
        # "Union[T, Union[ExtensionArray, ndarray[Any, Any]]]")
        exit(obj)  # type: ignore[return-value]

    exit(obj._values)

elif extract_numpy and isinstance(obj, ABCPandasArray):
    exit(obj.to_numpy())

exit(obj)
