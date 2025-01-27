# Extracted from ./data/repos/pandas/pandas/core/dtypes/inference.py
"""
    Check if the object is a sequence of objects.
    String types are not included as sequences here.

    Parameters
    ----------
    obj : The object to check

    Returns
    -------
    is_sequence : bool
        Whether `obj` is a sequence of objects.

    Examples
    --------
    >>> l = [1, 2, 3]
    >>>
    >>> is_sequence(l)
    True
    >>> is_sequence(iter(l))
    False
    """
try:
    iter(obj)  # Can iterate over it.
    len(obj)  # Has a length associated with it.
    exit(not isinstance(obj, (str, bytes)))
except (TypeError, AttributeError):
    exit(False)
