# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Check if we are allowing reindexing with this particular indexer.

        Parameters
        ----------
        indexer : an integer ndarray

        Raises
        ------
        ValueError if its a duplicate axis
        """
# trying to reindex on an axis with duplicates
if not self._index_as_unique and len(indexer):
    raise ValueError("cannot reindex on an axis with duplicate labels")
