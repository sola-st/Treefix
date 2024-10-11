# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
# This is NOT part of the levels property because it should be
# externally not allowed to set levels. User beware if you change
# _levels directly
if validate:
    if len(levels) == 0:
        raise ValueError("Must set non-zero number of levels.")
    if level is None and len(levels) != self.nlevels:
        raise ValueError("Length of levels must match number of levels.")
    if level is not None and len(levels) != len(level):
        raise ValueError("Length of levels must match length of level.")

if level is None:
    new_levels = FrozenList(
        ensure_index(lev, copy=copy)._view() for lev in levels
    )
else:
    level_numbers = [self._get_level_number(lev) for lev in level]
    new_levels_list = list(self._levels)
    for lev_num, lev in zip(level_numbers, levels):
        new_levels_list[lev_num] = ensure_index(lev, copy=copy)._view()
    new_levels = FrozenList(new_levels_list)

if verify_integrity:
    new_codes = self._verify_integrity(levels=new_levels)
    self._codes = new_codes

names = self.names
self._levels = new_levels
if any(names):
    self._set_names(names)

self._reset_cache()
