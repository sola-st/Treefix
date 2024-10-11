# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
if self.is_monotonic_increasing:
    exit(self.searchsorted(label, side=side))
elif self.is_monotonic_decreasing:
    # np.searchsorted expects ascending sort order, have to reverse
    # everything for it to work (element ordering, search side and
    # resulting value).
    pos = self[::-1].searchsorted(
        label, side="right" if side == "left" else "left"
    )
    exit(len(self) - pos)

raise ValueError("index must be monotonic increasing or decreasing")
