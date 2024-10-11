# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
(n_rows,) = self.shape
assert len(self.arrays) == 1
arr = self.arrays[0]
assert len(arr) == n_rows
if not arr.ndim == 1:
    raise ValueError(
        "Passed array should be 1-dimensional, got array with "
        f"{arr.ndim} dimensions instead."
    )
