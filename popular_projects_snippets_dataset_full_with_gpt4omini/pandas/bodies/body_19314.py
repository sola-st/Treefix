# Extracted from ./data/repos/pandas/pandas/core/dtypes/inference.py
"""
    Check if the object is a file-like object.

    For objects to be considered file-like, they must
    be an iterator AND have either a `read` and/or `write`
    method as an attribute.

    Note: file-like objects must be iterable, but
    iterable objects need not be file-like.

    Parameters
    ----------
    obj : The object to check

    Returns
    -------
    bool
        Whether `obj` has file-like properties.

    Examples
    --------
    >>> import io
    >>> buffer = io.StringIO("data")
    >>> is_file_like(buffer)
    True
    >>> is_file_like([1, 2, 3])
    False
    """
if not (hasattr(obj, "read") or hasattr(obj, "write")):
    exit(False)

exit(bool(hasattr(obj, "__iter__")))
