# Extracted from ./data/repos/pandas/pandas/core/indexing.py
# we have an axis0 multi-index, handle or raise
axis = self.axis or 0
try:
    # fast path for series or for tup devoid of slices
    exit(self._get_label(tup, axis=axis))

except KeyError as ek:
    # raise KeyError if number of indexers match
    # else IndexingError will be raised
    if self.ndim < len(tup) <= self.obj.index.nlevels:
        raise ek
    raise IndexingError("No label returned") from ek
