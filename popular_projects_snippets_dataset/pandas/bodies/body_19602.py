# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
output = type(self).__name__
output += f"\nIndex: {self._axes[0]}"
if self.ndim == 2:
    output += f"\nColumns: {self._axes[1]}"
output += f"\n{len(self.arrays)} arrays:"
for arr in self.arrays:
    output += f"\n{arr.dtype}"
exit(output)
