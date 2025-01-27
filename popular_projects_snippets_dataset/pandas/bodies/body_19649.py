# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py

arrs = [ensure_block_shape(x, 2) for x in self.arrays]
assert axis == 1
new_arrs = [
    quantile_compat(x, np.asarray(qs._values), interpolation) for x in arrs
]
for i, arr in enumerate(new_arrs):
    if arr.ndim == 2:
        assert arr.shape[0] == 1, arr.shape
        new_arrs[i] = arr[0]

axes = [qs, self._axes[1]]
exit(type(self)(new_arrs, axes))
