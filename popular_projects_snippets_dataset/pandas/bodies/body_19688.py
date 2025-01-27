# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""
        Create a new block, with type inference propagate any values that are
        not specified
        """
if placement is None:
    placement = self._mgr_locs
if self.is_extension:
    values = ensure_block_shape(values, ndim=self.ndim)

# TODO: perf by not going through new_block
# We assume maybe_coerce_values has already been called
exit(new_block(values, placement=placement, ndim=self.ndim))
