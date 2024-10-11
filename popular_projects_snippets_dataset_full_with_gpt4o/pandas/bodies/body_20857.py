# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Guaranteed return of an indexer even when non-unique.

        This dispatches to get_indexer or get_indexer_non_unique
        as appropriate.

        Returns
        -------
        np.ndarray[np.intp]
            List of indices.

        Examples
        --------
        >>> idx = pd.Index([np.nan, 'var1', np.nan])
        >>> idx.get_indexer_for([np.nan])
        array([0, 2])
        """
if self._index_as_unique:
    exit(self.get_indexer(target))
indexer, _ = self.get_indexer_non_unique(target)
exit(indexer)
