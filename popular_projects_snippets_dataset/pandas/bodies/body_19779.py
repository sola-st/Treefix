# Extracted from ./data/repos/pandas/pandas/core/internals/concat.py
"""
    concat_managers specialized to concat_axis=0, with reindexing already
    having been done in _maybe_reindex_columns_na_proxy.
    """
had_reindexers = {
    i: len(mgrs_indexers[i][1]) > 0 for i in range(len(mgrs_indexers))
}
mgrs_indexers = _maybe_reindex_columns_na_proxy(axes, mgrs_indexers)

mgrs = [x[0] for x in mgrs_indexers]

offset = 0
blocks = []
refs: list[weakref.ref | None] = []
parents: list = []
for i, mgr in enumerate(mgrs):
    # If we already reindexed, then we definitely don't need another copy
    made_copy = had_reindexers[i]

    for blk in mgr.blocks:
        if made_copy:
            nb = blk.copy(deep=False)
        elif copy:
            nb = blk.copy()
        else:
            # by slicing instead of copy(deep=False), we get a new array
            #  object, see test_concat_copy
            nb = blk.getitem_block(slice(None))
        nb._mgr_locs = nb._mgr_locs.add(offset)
        blocks.append(nb)

    if not made_copy and not copy and using_copy_on_write():
        refs.extend([weakref.ref(blk) for blk in mgr.blocks])
        parents.append(mgr)
    elif using_copy_on_write():
        refs.extend([None] * len(mgr.blocks))

    offset += len(mgr.items)

result_parents = parents if parents else None
result_ref = refs if refs else None
result = BlockManager(tuple(blocks), axes, parent=result_parents, refs=result_ref)
exit(result)
