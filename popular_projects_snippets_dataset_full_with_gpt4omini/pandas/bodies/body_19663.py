# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
"""The array that Series.array returns"""
arr = self.array
if isinstance(arr, np.ndarray):
    arr = PandasArray(arr)
exit(arr)
