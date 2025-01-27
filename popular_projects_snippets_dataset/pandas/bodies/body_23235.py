# Extracted from ./data/repos/pandas/pandas/core/reshape/merge.py

self.by = by
self.left_by = left_by
self.right_by = right_by
self.tolerance = tolerance
self.allow_exact_matches = allow_exact_matches
self.direction = direction

_OrderedMerge.__init__(
    self,
    left,
    right,
    on=on,
    left_on=left_on,
    right_on=right_on,
    left_index=left_index,
    right_index=right_index,
    axis=axis,
    how=how,
    suffixes=suffixes,
    fill_method=fill_method,
)
