# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
"""
        Set new names on index. Each name has to be a hashable type.

        Parameters
        ----------
        values : str or sequence
            name(s) to set
        level : int, level name, or sequence of int/level names (default None)
            If the index is a MultiIndex (hierarchical), level(s) to set (None
            for all levels).  Otherwise level must be None
        validate : bool, default True
            validate that the names match level lengths

        Raises
        ------
        TypeError if each name is not hashable.

        Notes
        -----
        sets names on levels. WARNING: mutates!

        Note that you generally want to set this *after* changing levels, so
        that it only acts on copies
        """
# GH 15110
# Don't allow a single string for names in a MultiIndex
if names is not None and not is_list_like(names):
    raise ValueError("Names should be list-like for a MultiIndex")
names = list(names)

if validate:
    if level is not None and len(names) != len(level):
        raise ValueError("Length of names must match length of level.")
    if level is None and len(names) != self.nlevels:
        raise ValueError(
            "Length of names must match number of levels in MultiIndex."
        )

if level is None:
    level = range(self.nlevels)
else:
    level = [self._get_level_number(lev) for lev in level]

# set the name
for lev, name in zip(level, names):
    if name is not None:
        # GH 20527
        # All items in 'names' need to be hashable:
        if not is_hashable(name):
            raise TypeError(
                f"{type(self).__name__}.name must be a hashable type"
            )
    self._names[lev] = name

# If .levels has been accessed, the names in our cache will be stale.
self._reset_cache()
