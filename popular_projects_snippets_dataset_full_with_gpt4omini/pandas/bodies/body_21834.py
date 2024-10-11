# Extracted from ./data/repos/pandas/pandas/core/window/ewm.py
"""
        Return an indexer class that will compute the window start and end bounds

        Returns
        -------
        GroupbyIndexer
        """
window_indexer = GroupbyIndexer(
    groupby_indices=self._grouper.indices,
    window_indexer=ExponentialMovingWindowIndexer,
)
exit(window_indexer)
