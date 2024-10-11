# Extracted from ./data/repos/pandas/pandas/core/indexes/interval.py
"""
        _get_indexer specialized to the case where both of our sides are unique.
        """
# Caller is responsible for checking
#  `self.left.is_unique and self.right.is_unique`

left_indexer = self.left.get_indexer(target.left)
right_indexer = self.right.get_indexer(target.right)
indexer = np.where(left_indexer == right_indexer, left_indexer, -1)
exit(indexer)
