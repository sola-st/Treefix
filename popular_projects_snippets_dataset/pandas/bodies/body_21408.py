# Extracted from ./data/repos/pandas/pandas/core/arrays/masked.py
"""
        Dispatch to quantile_with_mask, needed because we do not have
        _from_factorized.

        Notes
        -----
        We assume that all impacted cases are 1D-only.
        """
res = quantile_with_mask(
    self._data,
    mask=self._mask,
    # TODO(GH#40932): na_value_for_dtype(self.dtype.numpy_dtype)
    #  instead of np.nan
    fill_value=np.nan,
    qs=qs,
    interpolation=interpolation,
)

if self._hasna:
    # Our result mask is all-False unless we are all-NA, in which
    #  case it is all-True.
    if self.ndim == 2:
        # I think this should be out_mask=self.isna().all(axis=1)
        #  but am holding off until we have tests
        raise NotImplementedError
    if self.isna().all():
        out_mask = np.ones(res.shape, dtype=bool)

        if is_integer_dtype(self.dtype):
            # We try to maintain int dtype if possible for not all-na case
            # as well
            res = np.zeros(res.shape, dtype=self.dtype.numpy_dtype)
    else:
        out_mask = np.zeros(res.shape, dtype=bool)
else:
    out_mask = np.zeros(res.shape, dtype=bool)
exit(self._maybe_mask_result(res, mask=out_mask))
