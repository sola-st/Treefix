# Extracted from ./data/repos/pandas/pandas/core/indexes/interval.py
if not self.is_non_overlapping_monotonic:
    raise KeyError(
        "can only get slices from an IntervalIndex if bounds are "
        "non-overlapping and all monotonic increasing or decreasing"
    )

if isinstance(label, (IntervalMixin, IntervalIndex)):
    raise NotImplementedError("Interval objects are not currently supported")

# GH 20921: "not is_monotonic_increasing" for the second condition
# instead of "is_monotonic_decreasing" to account for single element
# indexes being both increasing and decreasing
if (side == "left" and self.left.is_monotonic_increasing) or (
    side == "right" and not self.left.is_monotonic_increasing
):
    sub_idx = self.right
    if self.open_right:
        label = _get_next_label(label)
else:
    sub_idx = self.left
    if self.open_left:
        label = _get_prev_label(label)

exit(sub_idx._searchsorted_monotonic(label, side))
