# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
"""
        Delete selected locations in-place (new array, same ArrayManager)
        """
to_keep = np.ones(self.shape[0], dtype=np.bool_)
to_keep[indexer] = False

self.arrays = [self.arrays[0][to_keep]]
self._axes = [self._axes[0][to_keep]]
exit(self)
