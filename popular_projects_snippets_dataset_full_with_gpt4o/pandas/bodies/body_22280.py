# Extracted from ./data/repos/pandas/pandas/core/resample.py
self.groupby = groupby
self.keys = None
self.sort = True
# error: Incompatible types in assignment (expression has type "Union
# [int, Literal['index', 'columns', 'rows']]", variable has type "int")
self.axis = axis  # type: ignore[assignment]
self.kind = kind
self.group_keys = group_keys
self.as_index = True

self.groupby._set_grouper(self._convert_obj(obj), sort=True)
self.binner, self.grouper = self._get_binner()
self._selection = selection
if self.groupby.key is not None:
    self.exclusions = frozenset([self.groupby.key])
else:
    self.exclusions = frozenset()
