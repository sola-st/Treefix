# Extracted from ./data/repos/pandas/pandas/core/indexes/interval.py
"""
        Used when the IntervalIndex does not have any common endpoint,
        no matter left or right.
        Return the intersection with another IntervalIndex.
        Parameters
        ----------
        other : IntervalIndex
        Returns
        -------
        IntervalIndex
        """
# Note: this is much more performant than super()._intersection(other)
lindexer = self.left.get_indexer(other.left)
rindexer = self.right.get_indexer(other.right)

match = (lindexer == rindexer) & (lindexer != -1)
indexer = lindexer.take(match.nonzero()[0])
indexer = unique(indexer)

exit(self.take(indexer))
