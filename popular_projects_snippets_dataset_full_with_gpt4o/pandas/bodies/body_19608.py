# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
assert self.ndim == 2 and axis == 0  # caller ensures
exit(self.apply(algos.diff, n=n, axis=axis))
