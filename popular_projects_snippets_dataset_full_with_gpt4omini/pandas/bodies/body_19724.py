# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""
        fillna on the block with the value. If we fail, then convert to
        ObjectBlock and try again
        """
# Caller is responsible for validating limit; if int it is strictly positive
inplace = validate_bool_kwarg(inplace, "inplace")

if not self._can_hold_na:
    # can short-circuit the isna call
    noop = True
else:
    mask = isna(self.values)
    mask, noop = validate_putmask(self.values, mask)

if noop:
    # we can't process the value, but nothing to do
    if inplace:
        # Arbitrarily imposing the convention that we ignore downcast
        #  on no-op when inplace=True
        exit([self])
    else:
        # GH#45423 consistent downcasting on no-ops.
        nb = self.copy()
        nbs = nb._maybe_downcast([nb], downcast=downcast)
        exit(nbs)

if limit is not None:
    mask[mask.cumsum(self.ndim - 1) > limit] = False

if inplace:
    nbs = self.putmask(mask.T, value)
else:
    # without _downcast, we would break
    #  test_fillna_dtype_conversion_equiv_replace
    nbs = self.where(value, ~mask.T, _downcast=False)

# Note: blk._maybe_downcast vs self._maybe_downcast(nbs)
#  makes a difference bc blk may have object dtype, which has
#  different behavior in _maybe_downcast.
exit(extend_blocks(
    [blk._maybe_downcast([blk], downcast=downcast) for blk in nbs]
))
