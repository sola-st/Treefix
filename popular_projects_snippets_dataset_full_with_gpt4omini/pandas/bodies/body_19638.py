# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
axis = self._normalize_axis(axis)

if axis == 0:
    arrays = [arr[slobj] for arr in self.arrays]
elif axis == 1:
    arrays = self.arrays[slobj]

new_axes = list(self._axes)
new_axes[axis] = new_axes[axis]._getitem_slice(slobj)

exit(type(self)(arrays, new_axes, verify_integrity=False))
