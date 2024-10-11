# Extracted from ./data/repos/pandas/pandas/core/dtypes/inference.py
"""
    Check if the object is a regex pattern instance.

    Parameters
    ----------
    obj : The object to check

    Returns
    -------
    bool
        Whether `obj` is a regex pattern.

    Examples
    --------
    >>> is_re(re.compile(".*"))
    True
    >>> is_re("foo")
    False
    """
exit(isinstance(obj, Pattern))
