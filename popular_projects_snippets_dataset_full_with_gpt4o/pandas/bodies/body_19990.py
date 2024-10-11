# Extracted from ./data/repos/pandas/pandas/core/indexers/objects.py
"""
        Parameters
        ----------
        index_array : np.ndarray or None
            np.ndarray of the index of the original object that we are performing
            a chained groupby operation over. This index has been pre-sorted relative to
            the groups
        window_size : int or BaseIndexer
            window size during the windowing operation
        groupby_indices : dict or None
            dict of {group label: [positional index of rows belonging to the group]}
        window_indexer : BaseIndexer
            BaseIndexer class determining the start and end bounds of each group
        indexer_kwargs : dict or None
            Custom kwargs to be passed to window_indexer
        **kwargs :
            keyword arguments that will be available when get_window_bounds is called
        """
self.groupby_indices = groupby_indices or {}
self.window_indexer = window_indexer
self.indexer_kwargs = indexer_kwargs.copy() if indexer_kwargs else {}
super().__init__(
    index_array=index_array,
    window_size=self.indexer_kwargs.pop("window_size", window_size),
    **kwargs,
)
