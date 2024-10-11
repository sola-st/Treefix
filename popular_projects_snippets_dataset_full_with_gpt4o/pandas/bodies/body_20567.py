# Extracted from ./data/repos/pandas/pandas/core/indexes/interval.py
"""
        Used when the IntervalIndex does have some common endpoints,
        on either sides.
        Return the intersection with another IntervalIndex.

        Parameters
        ----------
        other : IntervalIndex

        Returns
        -------
        IntervalIndex
        """
# Note: this is about 3.25x faster than super()._intersection(other)
#  in IntervalIndexMethod.time_intersection_both_duplicate(1000)
mask = np.zeros(len(self), dtype=bool)

if self.hasnans and other.hasnans:
    first_nan_loc = np.arange(len(self))[self.isna()][0]
    mask[first_nan_loc] = True

other_tups = set(zip(other.left, other.right))
for i, tup in enumerate(zip(self.left, self.right)):
    if tup in other_tups:
        mask[i] = True

exit(self[mask])
