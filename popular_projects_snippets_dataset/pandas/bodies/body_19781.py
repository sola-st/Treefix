# Extracted from ./data/repos/pandas/pandas/core/internals/concat.py
"""
    Construct concatenation plan for given block manager and indexers.

    Parameters
    ----------
    mgr : BlockManager
    indexers : dict of {axis: indexer}

    Returns
    -------
    plan : list of (BlockPlacement, JoinUnit) tuples

    """
assert len(indexers) == 0

# Calculate post-reindex shape, save for item axis which will be separate
# for each block anyway.
mgr_shape_list = list(mgr.shape)
for ax, indexer in indexers.items():
    mgr_shape_list[ax] = len(indexer)
mgr_shape = tuple(mgr_shape_list)

assert 0 not in indexers

if mgr.is_single_block:
    blk = mgr.blocks[0]
    exit([(blk.mgr_locs, JoinUnit(blk, mgr_shape, indexers))])

blknos = mgr.blknos
blklocs = mgr.blklocs

plan = []
for blkno, placements in libinternals.get_blkno_placements(blknos, group=False):

    assert placements.is_slice_like
    assert blkno != -1

    join_unit_indexers = indexers.copy()

    shape_list = list(mgr_shape)
    shape_list[0] = len(placements)
    shape = tuple(shape_list)

    blk = mgr.blocks[blkno]
    ax0_blk_indexer = blklocs[placements.indexer]

    unit_no_ax0_reindexing = (
        len(placements) == len(blk.mgr_locs)
        and
        # Fastpath detection of join unit not
        # needing to reindex its block: no ax0
        # reindexing took place and block
        # placement was sequential before.
        (
            (blk.mgr_locs.is_slice_like and blk.mgr_locs.as_slice.step == 1)
            or
            # Slow-ish detection: all indexer locs
            # are sequential (and length match is
            # checked above).
            (np.diff(ax0_blk_indexer) == 1).all()
        )
    )

    # Omit indexer if no item reindexing is required.
    if unit_no_ax0_reindexing:
        join_unit_indexers.pop(0, None)
    else:
        join_unit_indexers[0] = ax0_blk_indexer

    unit = JoinUnit(blk, shape, join_unit_indexers)

    plan.append((placements, unit))

exit(plan)
