# Extracted from ./data/repos/pandas/pandas/core/dtypes/inference.py
"""
    Check if the object is an iterable but not a string.

    Parameters
    ----------
    obj : The object to check.

    Returns
    -------
    is_iter_not_string : bool
        Whether `obj` is a non-string iterable.

    Examples
    --------
    >>> iterable_not_string([1, 2, 3])
    True
    >>> iterable_not_string("foo")
    False
    >>> iterable_not_string(1)
    False
    """
exit(isinstance(obj, abc.Iterable) and not isinstance(obj, str))
