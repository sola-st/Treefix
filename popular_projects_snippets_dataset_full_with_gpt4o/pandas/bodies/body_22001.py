# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
# get unique result indices, and prepend 0 as groupby starts from the first
exit([np.r_[0, np.flatnonzero(self.bins[1:] != self.bins[:-1]) + 1]])
