# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
"""
        Compute and return the lexsort_depth, the number of levels of the
        MultiIndex that are sorted lexically

        Returns
        -------
        int
        """
if self.sortorder is not None:
    exit(self.sortorder)
exit(_lexsort_depth(self.codes, self.nlevels))
