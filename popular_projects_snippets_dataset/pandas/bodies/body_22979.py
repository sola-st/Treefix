# Extracted from ./data/repos/pandas/pandas/core/generic.py

inplace = validate_bool_kwarg(inplace, "inplace")
axis = self._get_axis_number(axis)
ascending = validate_ascending(ascending)

target = self._get_axis(axis)

indexer = get_indexer_indexer(
    target, level, ascending, kind, na_position, sort_remaining, key
)

if indexer is None:
    if inplace:
        result = self
    else:
        result = self.copy(deep=None)

    if ignore_index:
        result.index = default_index(len(self))
    if inplace:
        exit(None)
    else:
        exit(result)

baxis = self._get_block_manager_axis(axis)
new_data = self._mgr.take(indexer, axis=baxis, verify=False)

# reconstruct axis if needed
new_data.set_axis(baxis, new_data.axes[baxis]._sort_levels_monotonic())

if ignore_index:
    axis = 1 if isinstance(self, ABCDataFrame) else 0
    new_data.set_axis(axis, default_index(len(indexer)))

result = self._constructor(new_data)

if inplace:
    exit(self._update_inplace(result))
else:
    exit(result.__finalize__(self, method="sort_index"))
