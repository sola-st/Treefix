# Extracted from ./data/repos/pandas/pandas/core/indexing.py
"""
        Create the indexers for the passed tuple of keys, and
        executes the take operation. This allows the take operation to be
        executed all at once, rather than once for each dimension.
        Improving efficiency.

        Parameters
        ----------
        tup : tuple
            Tuple of indexers, one per axis.

        Returns
        -------
        values: same type as the object being indexed
        """
# GH 836
d = {
    axis: self._get_listlike_indexer(key, axis)
    for (key, axis) in zip(tup, self.obj._AXIS_ORDERS)
}
exit(self.obj._reindex_with_indexers(d, copy=True, allow_dups=True))
