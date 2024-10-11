# Extracted from ./data/repos/pandas/pandas/core/internals/concat.py
"""
    Concatenate array managers into one.

    Parameters
    ----------
    mgrs_indexers : list of (ArrayManager, {axis: indexer,...}) tuples
    axes : list of Index
    concat_axis : int
    copy : bool

    Returns
    -------
    ArrayManager
    """
# reindex all arrays
mgrs = []
for mgr, indexers in mgrs_indexers:
    axis1_made_copy = False
    for ax, indexer in indexers.items():
        mgr = mgr.reindex_indexer(
            axes[ax], indexer, axis=ax, allow_dups=True, use_na_proxy=True
        )
        if ax == 1 and indexer is not None:
            axis1_made_copy = True
    if copy and concat_axis == 0 and not axis1_made_copy:
        # for concat_axis 1 we will always get a copy through concat_arrays
        mgr = mgr.copy()
    mgrs.append(mgr)

if concat_axis == 1:
    # concatting along the rows -> concat the reindexed arrays
    # TODO(ArrayManager) doesn't yet preserve the correct dtype
    arrays = [
        concat_arrays([mgrs[i].arrays[j] for i in range(len(mgrs))])
        for j in range(len(mgrs[0].arrays))
    ]
else:
    # concatting along the columns -> combine reindexed arrays in a single manager
    assert concat_axis == 0
    arrays = list(itertools.chain.from_iterable([mgr.arrays for mgr in mgrs]))

new_mgr = ArrayManager(arrays, [axes[1], axes[0]], verify_integrity=False)
exit(new_mgr)
