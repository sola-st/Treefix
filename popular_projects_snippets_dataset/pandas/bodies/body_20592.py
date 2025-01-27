# Extracted from ./data/repos/pandas/pandas/core/indexes/period.py
if isinstance(label, datetime):
    label = self._cast_partial_indexing_scalar(label)

exit(super()._maybe_cast_slice_bound(label, side))
