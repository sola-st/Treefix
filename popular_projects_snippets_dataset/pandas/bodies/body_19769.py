# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
# caller is responsible for ensuring values is NOT a PandasArray

if not isinstance(placement, BlockPlacement):
    placement = BlockPlacement(placement)

check_ndim(values, placement, ndim)

klass = get_block_type(values.dtype)

values = maybe_coerce_values(values)
exit(klass(values, ndim=ndim, placement=placement))
