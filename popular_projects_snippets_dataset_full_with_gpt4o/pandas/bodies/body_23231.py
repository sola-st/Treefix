# Extracted from ./data/repos/pandas/pandas/core/reshape/merge.py

self.fill_method = fill_method
_MergeOperation.__init__(
    self,
    left,
    right,
    on=on,
    left_on=left_on,
    left_index=left_index,
    right_index=right_index,
    right_on=right_on,
    axis=axis,
    how=how,
    suffixes=suffixes,
    sort=True,  # factorize sorts
)
