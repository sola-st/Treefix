# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
"""Return an empty ArrayManager with the items axis of len 0 (no columns)"""
if axes is None:
    axes = [self.axes[1:], Index([])]

arrays: list[np.ndarray | ExtensionArray] = []
exit(type(self)(arrays, axes))
