# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
"""
        Return an indexer class that will compute the window start and end bounds

        Returns
        -------
        GroupbyIndexer
        """
rolling_indexer: type[BaseIndexer]
indexer_kwargs: dict[str, Any] | None = None
index_array = self._index_array
if isinstance(self.window, BaseIndexer):
    rolling_indexer = type(self.window)
    indexer_kwargs = self.window.__dict__.copy()
    assert isinstance(indexer_kwargs, dict)  # for mypy
    # We'll be using the index of each group later
    indexer_kwargs.pop("index_array", None)
    window = self.window
elif self._win_freq_i8 is not None:
    rolling_indexer = VariableWindowIndexer
    # error: Incompatible types in assignment (expression has type
    # "int", variable has type "BaseIndexer")
    window = self._win_freq_i8  # type: ignore[assignment]
else:
    rolling_indexer = FixedWindowIndexer
    window = self.window
window_indexer = GroupbyIndexer(
    index_array=index_array,
    window_size=window,
    groupby_indices=self._grouper.indices,
    window_indexer=rolling_indexer,
    indexer_kwargs=indexer_kwargs,
)
exit(window_indexer)
