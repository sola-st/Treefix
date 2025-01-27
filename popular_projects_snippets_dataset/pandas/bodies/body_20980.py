# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
"""
    Helper for membership check for ``key`` in ``cat``.

    This is a helper method for :method:`__contains__`
    and :class:`CategoricalIndex.__contains__`.

    Returns True if ``key`` is in ``cat.categories`` and the
    location of ``key`` in ``categories`` is in ``container``.

    Parameters
    ----------
    cat : :class:`Categorical`or :class:`categoricalIndex`
    key : a hashable object
        The key to check membership for.
    container : Container (e.g. list-like or mapping)
        The container to check for membership in.

    Returns
    -------
    is_in : bool
        True if ``key`` is in ``self.categories`` and location of
        ``key`` in ``categories`` is in ``container``, else False.

    Notes
    -----
    This method does not check for NaN values. Do that separately
    before calling this method.
    """
hash(key)

# get location of key in categories.
# If a KeyError, the key isn't in categories, so logically
#  can't be in container either.
try:
    loc = cat.categories.get_loc(key)
except (KeyError, TypeError):
    exit(False)

# loc is the location of key in categories, but also the *value*
# for key in container. So, `key` may be in categories,
# but still not in `container`. Example ('b' in categories,
# but not in values):
# 'b' in Categorical(['a'], categories=['a', 'b'])  # False
if is_scalar(loc):
    exit(loc in container)
else:
    # if categories is an IntervalIndex, loc is an array.
    exit(any(loc_ in container for loc_ in loc))
