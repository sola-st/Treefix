# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
# new_block specialized to case with
#  ndim=2
#  isinstance(placement, BlockPlacement)
#  check_ndim/ensure_block_shape already checked
klass = get_block_type(values.dtype)

values = maybe_coerce_values(values)
exit(klass(values, ndim=2, placement=placement))
