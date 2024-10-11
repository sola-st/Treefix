# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
self.bins = ensure_int64(bins)
self.binlabels = ensure_index(binlabels)
self.mutated = mutated
self.indexer = indexer

# These lengths must match, otherwise we could call agg_series
#  with empty self.bins, which would raise in libreduction.
assert len(self.binlabels) == len(self.bins)
