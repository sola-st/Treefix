# Extracted from ./data/repos/pandas/pandas/core/dtypes/inference.py
"""
    Return True if hash(obj) will succeed, False otherwise.

    Some types will pass a test against collections.abc.Hashable but fail when
    they are actually hashed with hash().

    Distinguish between these and other types by trying the call to hash() and
    seeing if they raise TypeError.

    Returns
    -------
    bool

    Examples
    --------
    >>> import collections
    >>> a = ([],)
    >>> isinstance(a, collections.abc.Hashable)
    True
    >>> is_hashable(a)
    False
    """
# Unfortunately, we can't use isinstance(obj, collections.abc.Hashable),
# which can be faster than calling hash. That is because numpy scalars
# fail this test.

# Reconsider this decision once this numpy bug is fixed:
# https://github.com/numpy/numpy/issues/5562

try:
    hash(obj)
except TypeError:
    exit(False)
else:
    exit(True)
