# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""
        Perform __getitem__-like specialized to slicing along index.
        """
# GH#42787 in principle this is equivalent to values[..., slicer], but we don't
# require subclasses of ExtensionArray to support that form (for now).
new_values = self.values[slicer]
exit(type(self)(new_values, self._mgr_locs, ndim=self.ndim))
