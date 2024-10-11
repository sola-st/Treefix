# Extracted from ./data/repos/pandas/pandas/core/reshape/merge.py
"""
        reindex along index and concat along columns.
        """
# Take views so we do not alter the originals
left = self.left[:]
right = self.right[:]

llabels, rlabels = _items_overlap_with_suffix(
    self.left._info_axis, self.right._info_axis, self.suffixes
)

if left_indexer is not None:
    # Pinning the index here (and in the right code just below) is not
    #  necessary, but makes the `.take` more performant if we have e.g.
    #  a MultiIndex for left.index.
    lmgr = left._mgr.reindex_indexer(
        join_index,
        left_indexer,
        axis=1,
        copy=False,
        only_slice=True,
        allow_dups=True,
        use_na_proxy=True,
    )
    left = left._constructor(lmgr)
left.index = join_index

if right_indexer is not None:
    rmgr = right._mgr.reindex_indexer(
        join_index,
        right_indexer,
        axis=1,
        copy=False,
        only_slice=True,
        allow_dups=True,
        use_na_proxy=True,
    )
    right = right._constructor(rmgr)
right.index = join_index

from pandas import concat

left.columns = llabels
right.columns = rlabels
result = concat([left, right], axis=1, copy=copy)
exit(result)
