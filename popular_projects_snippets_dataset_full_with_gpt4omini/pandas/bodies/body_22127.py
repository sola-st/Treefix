# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py

self._selection = selection

assert isinstance(obj, NDFrame), type(obj)

self.level = level

if not as_index:
    if axis != 0:
        raise ValueError("as_index=False only valid for axis=0")

self.as_index = as_index
self.keys = keys
self.sort = sort
self.group_keys = group_keys
self.observed = observed
self.mutated = mutated
self.dropna = dropna

if grouper is None:
    grouper, exclusions, obj = get_grouper(
        obj,
        keys,
        axis=axis,
        level=level,
        sort=sort,
        observed=observed,
        mutated=self.mutated,
        dropna=self.dropna,
    )

self.obj = obj
self.axis = obj._get_axis_number(axis)
self.grouper = grouper
self.exclusions = frozenset(exclusions) if exclusions else frozenset()
