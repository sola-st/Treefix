# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
assert isinstance(axis, Index), axis

self.axis = axis
self._groupings: list[grouper.Grouping] = list(groupings)
self._sort = sort
self.group_keys = group_keys
self.mutated = mutated
self.indexer = indexer
self.dropna = dropna
