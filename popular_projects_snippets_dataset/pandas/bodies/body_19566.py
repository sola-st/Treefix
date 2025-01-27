# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
# Assertion disabled for performance
# assert isinstance(slobj, slice), type(slobj)
if axis >= self.ndim:
    raise IndexError("Requested axis not found in manager")

blk = self._block
array = blk._slice(slobj)
bp = BlockPlacement(slice(0, len(array)))
block = type(blk)(array, placement=bp, ndim=1)
new_index = self.index._getitem_slice(slobj)
# TODO this method is only used in groupby SeriesSplitter at the moment,
# so passing refs / parent is not yet covered by the tests
exit(type(self)(block, new_index, [weakref.ref(blk)], parent=self))
