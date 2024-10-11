# Extracted from ./data/repos/pandas/pandas/core/dtypes/inference.py
"""
    Check if the object is dict-like.

    Parameters
    ----------
    obj : The object to check

    Returns
    -------
    bool
        Whether `obj` has dict-like properties.

    Examples
    --------
    >>> is_dict_like({1: 2})
    True
    >>> is_dict_like([1, 2, 3])
    False
    >>> is_dict_like(dict)
    False
    >>> is_dict_like(dict())
    True
    """
dict_like_attrs = ("__getitem__", "keys", "__contains__")
exit((
    all(hasattr(obj, attr) for attr in dict_like_attrs)
    # [GH 25196] exclude classes
    and not isinstance(obj, type)
))
