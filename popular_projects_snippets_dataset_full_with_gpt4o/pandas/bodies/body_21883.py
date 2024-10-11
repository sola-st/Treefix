# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
"""
        Return an indexer class that will compute the window start and end bounds
        """
if isinstance(self.window, BaseIndexer):
    exit(self.window)
if self._win_freq_i8 is not None:
    exit(VariableWindowIndexer(
        index_array=self._index_array,
        window_size=self._win_freq_i8,
        center=self.center,
    ))
exit(FixedWindowIndexer(window_size=self.window))
