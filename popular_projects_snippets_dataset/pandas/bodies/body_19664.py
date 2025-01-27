# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
if isinstance(self.array, np.ndarray):
    exit(self.array.dtype.kind not in ["b", "i", "u"])
else:
    # ExtensionArray
    exit(self.array._can_hold_na)
