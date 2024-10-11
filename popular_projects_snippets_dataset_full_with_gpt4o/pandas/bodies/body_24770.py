# Extracted from ./data/repos/pandas/pandas/io/formats/info.py
self.info = info
self.data = info.data
self.verbose = verbose
self.max_cols = self._initialize_max_cols(max_cols)
self.show_counts = self._initialize_show_counts(show_counts)
