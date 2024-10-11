# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""
        compute the quantiles of the

        Parameters
        ----------
        qs : Index
            The quantiles to be computed in float64.
        interpolation : str, default 'linear'
            Type of interpolation.
        axis : int, default 0
            Axis to compute.

        Returns
        -------
        Block
        """
# We should always have ndim == 2 because Series dispatches to DataFrame
assert self.ndim == 2
assert axis == 1  # only ever called this way
assert is_list_like(qs)  # caller is responsible for this

result = quantile_compat(self.values, np.asarray(qs._values), interpolation)
# ensure_block_shape needed for cases where we start with EA and result
#  is ndarray, e.g. IntegerArray, SparseArray
result = ensure_block_shape(result, ndim=2)
exit(new_block_2d(result, placement=self._mgr_locs))
