# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
# similar to get_slice, but not restricted to slice indexer
blk = self._block
if (
    using_copy_on_write()
    and isinstance(indexer, np.ndarray)
    and len(indexer) > 0
    and com.is_bool_indexer(indexer)
    and indexer.all()
):
    exit(type(self)(blk, self.index, [weakref.ref(blk)], parent=self))
array = blk._slice(indexer)
if array.ndim > 1:
    # This will be caught by Series._get_values
    raise ValueError("dimension-expanding indexing not allowed")

bp = BlockPlacement(slice(0, len(array)))
block = type(blk)(array, placement=bp, ndim=1)

new_idx = self.index[indexer]
# TODO(CoW) in theory only need to track reference if new_array is a view
ref = weakref.ref(blk)
exit(type(self)(block, new_idx, [ref], parent=self))
