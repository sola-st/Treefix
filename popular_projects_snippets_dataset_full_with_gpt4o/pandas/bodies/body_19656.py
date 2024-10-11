# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
"""Return an empty ArrayManager with index/array of length 0"""
if axes is None:
    axes = [Index([], dtype=object)]
array: np.ndarray = np.array([], dtype=self.dtype)
exit(type(self)([array], axes))
