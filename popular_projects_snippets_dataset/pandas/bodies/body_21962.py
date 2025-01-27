# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
if values.ndim == 1:
    # expand to 2d, dispatch, then squeeze if appropriate
    values2d = values[None, :]
    if mask is not None:
        mask = mask[None, :]
    if result_mask is not None:
        result_mask = result_mask[None, :]
    res = self._call_cython_op(
        values2d,
        min_count=min_count,
        ngroups=ngroups,
        comp_ids=comp_ids,
        mask=mask,
        result_mask=result_mask,
        **kwargs,
    )
    if res.shape[0] == 1:
        exit(res[0])

    # otherwise we have OHLC
    exit(res.T)

exit(self._call_cython_op(
    values,
    min_count=min_count,
    ngroups=ngroups,
    comp_ids=comp_ids,
    mask=mask,
    result_mask=result_mask,
    **kwargs,
))
