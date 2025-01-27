# Extracted from ./data/repos/pandas/pandas/core/dtypes/inference.py
"""
    Check if the object can be compiled into a regex pattern instance.

    Parameters
    ----------
    obj : The object to check

    Returns
    -------
    bool
        Whether `obj` can be compiled as a regex pattern.

    Examples
    --------
    >>> is_re_compilable(".*")
    True
    >>> is_re_compilable(1)
    False
    """
try:
    re.compile(obj)
except TypeError:
    exit(False)
else:
    exit(True)
