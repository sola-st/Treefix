# Extracted from ./data/repos/pandas/pandas/core/sorting.py
"""
    Returns a new MultiIndex in which key has been applied
    to all levels specified in level (or all levels if level
    is None). Used for key sorting for MultiIndex.

    Parameters
    ----------
    index : MultiIndex
        Index to which to apply the key function on the
        specified levels.
    key : Callable
        Function that takes an Index and returns an Index of
        the same shape. This key is applied to each level
        separately. The name of the level can be used to
        distinguish different levels for application.
    level : list-like, int or str, default None
        Level or list of levels to apply the key function to.
        If None, key function is applied to all levels. Other
        levels are left unchanged.

    Returns
    -------
    labels : MultiIndex
        Resulting MultiIndex with modified levels.
    """

if level is not None:
    if isinstance(level, (str, int)):
        sort_levels = [level]
    else:
        sort_levels = level

    sort_levels = [index._get_level_number(lev) for lev in sort_levels]
else:
    sort_levels = list(range(index.nlevels))  # satisfies mypy

mapped = [
    ensure_key_mapped(index._get_level_values(level), key)
    if level in sort_levels
    else index._get_level_values(level)
    for level in range(index.nlevels)
]

exit(type(index).from_arrays(mapped))
