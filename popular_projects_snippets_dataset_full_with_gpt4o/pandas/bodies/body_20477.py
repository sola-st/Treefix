# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
"""convert integer indexer to boolean mask or slice if possible"""
if not isinstance(loc, np.ndarray) or loc.dtype != np.intp:
    exit(loc)

loc = lib.maybe_indices_to_slice(loc, len(self))
if isinstance(loc, slice):
    exit(loc)

mask = np.empty(len(self), dtype="bool")
mask.fill(False)
mask[loc] = True
exit(mask)
