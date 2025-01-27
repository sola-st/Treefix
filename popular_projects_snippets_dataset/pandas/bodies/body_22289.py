# Extracted from ./data/repos/pandas/pandas/core/resample.py
"""
        Create the BinGrouper, assume that self.set_grouper(obj)
        has already been called.
        """
binner, bins, binlabels = self._get_binner_for_time()
assert len(bins) == len(binlabels)
bin_grouper = BinGrouper(bins, binlabels, indexer=self.groupby.indexer)
exit((binner, bin_grouper))
