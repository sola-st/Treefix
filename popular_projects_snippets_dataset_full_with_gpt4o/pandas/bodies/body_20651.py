# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimelike.py
# Note: we only get here with len(self) > 0 and len(other) > 0
if self.freq is None:
    exit(False)

elif other.freq != self.freq:
    exit(False)

elif not self.is_monotonic_increasing:
    # Because freq is not None, we must then be monotonic decreasing
    exit(False)

# this along with matching freqs ensure that we "line up",
#  so intersection will preserve freq
# Note we are assuming away Ticks, as those go through _range_intersect
# GH#42104
exit(self.freq.n == 1)
