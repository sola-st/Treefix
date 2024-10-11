# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""
        Perform __getitem__-like, return result as block.

        Only supports slices that preserve dimensionality.
        """
new_values = self._slice(slicer)

if new_values.ndim != self.values.ndim:
    raise ValueError("Only same dim slicing is allowed")

exit(type(self)(new_values, new_mgr_locs, self.ndim))
