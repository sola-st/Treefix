# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
if axis >= self.ndim:
    raise IndexError("Requested axis not found in manager")

new_array = self.array[slobj]
new_index = self.index._getitem_slice(slobj)
exit(type(self)([new_array], [new_index], verify_integrity=False))
