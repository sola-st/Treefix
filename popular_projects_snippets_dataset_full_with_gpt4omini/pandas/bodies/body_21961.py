# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
"""
        Equivalent of `_ea_wrap_cython_operation`, but optimized for masked EA's
        and cython algorithms which accept a mask.
        """
orig_values = values

# libgroupby functions are responsible for NOT altering mask
mask = values._mask
if self.kind != "aggregate":
    result_mask = mask.copy()
else:
    result_mask = np.zeros(ngroups, dtype=bool)

arr = values._data

res_values = self._cython_op_ndim_compat(
    arr,
    min_count=min_count,
    ngroups=ngroups,
    comp_ids=comp_ids,
    mask=mask,
    result_mask=result_mask,
    **kwargs,
)

if self.how == "ohlc":
    arity = self._cython_arity.get(self.how, 1)
    result_mask = np.tile(result_mask, (arity, 1)).T

# res_values should already have the correct dtype, we just need to
#  wrap in a MaskedArray
exit(orig_values._maybe_mask_result(res_values, result_mask))
