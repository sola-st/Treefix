# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
"""
        Delete selected locations, returning a new BlockManager.
        """
is_deleted = np.zeros(self.shape[0], dtype=np.bool_)
is_deleted[indexer] = True
taker = (~is_deleted).nonzero()[0]

nbs, new_refs = self._slice_take_blocks_ax0(taker, only_slice=True)
new_columns = self.items[~is_deleted]
axes = [new_columns, self.axes[1]]
# TODO this might not be needed (can a delete ever be done in chained manner?)
parent = None if com.all_none(*new_refs) else self
exit(type(self)(tuple(nbs), axes, new_refs, parent, verify_integrity=False))
