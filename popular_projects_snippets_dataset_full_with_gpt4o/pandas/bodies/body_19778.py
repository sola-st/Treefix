# Extracted from ./data/repos/pandas/pandas/core/internals/concat.py
"""
    Concatenate block managers into one.

    Parameters
    ----------
    mgrs_indexers : list of (BlockManager, {axis: indexer,...}) tuples
    axes : list of Index
    concat_axis : int
    copy : bool

    Returns
    -------
    BlockManager
    """
# TODO(ArrayManager) this assumes that all managers are of the same type
if isinstance(mgrs_indexers[0][0], ArrayManager):
    exit(_concatenate_array_managers(mgrs_indexers, axes, concat_axis, copy))

# Assertions disabled for performance
# for tup in mgrs_indexers:
#    # caller is responsible for ensuring this
#    indexers = tup[1]
#    assert concat_axis not in indexers

if concat_axis == 0:
    exit(_concat_managers_axis0(mgrs_indexers, axes, copy))

mgrs_indexers = _maybe_reindex_columns_na_proxy(axes, mgrs_indexers)

concat_plans = [
    _get_mgr_concatenation_plan(mgr, indexers) for mgr, indexers in mgrs_indexers
]
concat_plan = _combine_concat_plans(concat_plans)
blocks = []

for placement, join_units in concat_plan:
    unit = join_units[0]
    blk = unit.block

    if len(join_units) == 1 and not join_units[0].indexers:
        values = blk.values
        if copy:
            values = values.copy()
        else:
            values = values.view()
        fastpath = True
    elif _is_uniform_join_units(join_units):
        vals = [ju.block.values for ju in join_units]

        if not blk.is_extension:
            # _is_uniform_join_units ensures a single dtype, so
            #  we can use np.concatenate, which is more performant
            #  than concat_compat
            values = np.concatenate(vals, axis=1)
        else:
            # TODO(EA2D): special-casing not needed with 2D EAs
            values = concat_compat(vals, axis=1)
            values = ensure_block_shape(values, ndim=2)

        values = ensure_wrapped_if_datetimelike(values)

        fastpath = blk.values.dtype == values.dtype
    else:
        values = _concatenate_join_units(join_units, copy=copy)
        fastpath = False

    if fastpath:
        b = blk.make_block_same_class(values, placement=placement)
    else:
        b = new_block_2d(values, placement=placement)

    blocks.append(b)

exit(BlockManager(tuple(blocks), axes))
