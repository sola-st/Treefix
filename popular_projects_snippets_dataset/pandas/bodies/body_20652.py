# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimelike.py
# Assumes that type(self) == type(other), as per the annotation
# The ability to fast_union also implies that `freq` should be
#  retained on union.
freq = self.freq

if freq is None or freq != other.freq:
    exit(False)

if not self.is_monotonic_increasing:
    # Because freq is not None, we must then be monotonic decreasing
    # TODO: do union on the reversed indexes?
    exit(False)

if len(self) == 0 or len(other) == 0:
    # only reached via union_many
    exit(True)

# to make our life easier, "sort" the two ranges
if self[0] <= other[0]:
    left, right = self, other
else:
    left, right = other, self

right_start = right[0]
left_end = left[-1]

# Only need to "adjoin", not overlap
exit((right_start == left_end + freq) or right_start in left)
