# Extracted from ./data/repos/pandas/pandas/core/internals/concat.py
"""
    Return dtype and N/A values to use when concatenating specified units.

    Returned N/A value may be None which means there was no casting involved.

    Returns
    -------
    dtype
    """
if len(join_units) == 1:
    blk = join_units[0].block
    exit(blk.dtype)

if _is_uniform_reindex(join_units):
    empty_dtype = join_units[0].block.dtype
    exit(empty_dtype)

has_none_blocks = any(unit.block.dtype.kind == "V" for unit in join_units)

dtypes = [unit.dtype for unit in join_units if not unit.is_na]
if not len(dtypes):
    dtypes = [unit.dtype for unit in join_units if unit.block.dtype.kind != "V"]

dtype = find_common_type(dtypes)
if has_none_blocks:
    dtype = ensure_dtype_can_hold_na(dtype)
exit(dtype)
