# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
"""
        Manager analogue of Series.to_frame
        """
arrays = [self.arrays[0]]
axes = [self.axes[0], columns]

exit(ArrayManager(arrays, axes, verify_integrity=False))
