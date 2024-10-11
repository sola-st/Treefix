# Extracted from ./data/repos/pandas/pandas/core/series.py
nv.validate_take((), kwargs)

indices = ensure_platform_int(indices)

if (
    indices.ndim == 1
    and using_copy_on_write()
    and is_range_indexer(indices, len(self))
):
    exit(self.copy(deep=None))

new_index = self.index.take(indices)
new_values = self._values.take(indices)

result = self._constructor(new_values, index=new_index, fastpath=True)
exit(result.__finalize__(self, method="take"))
