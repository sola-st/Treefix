# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
"""
        If we have an ExtensionArray, unwrap, call _cython_operation, and
        re-wrap if appropriate.
        """
if isinstance(values, BaseMaskedArray):
    exit(self._masked_ea_wrap_cython_operation(
        values,
        min_count=min_count,
        ngroups=ngroups,
        comp_ids=comp_ids,
        **kwargs,
    ))

elif isinstance(values, Categorical):
    assert self.how == "rank"  # the only one implemented ATM
    assert values.ordered  # checked earlier
    mask = values.isna()
    npvalues = values._ndarray

    res_values = self._cython_op_ndim_compat(
        npvalues,
        min_count=min_count,
        ngroups=ngroups,
        comp_ids=comp_ids,
        mask=mask,
        **kwargs,
    )

    # If we ever have more than just "rank" here, we'll need to do
    #  `if self.how in self.cast_blocklist` like we do for other dtypes.
    exit(res_values)

npvalues = self._ea_to_cython_values(values)

res_values = self._cython_op_ndim_compat(
    npvalues,
    min_count=min_count,
    ngroups=ngroups,
    comp_ids=comp_ids,
    mask=None,
    **kwargs,
)

if self.how in self.cast_blocklist:
    # i.e. how in ["rank"], since other cast_blocklist methods don't go
    #  through cython_operation
    exit(res_values)

exit(self._reconstruct_ea_result(values, res_values))
