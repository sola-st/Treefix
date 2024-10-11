# Extracted from ./data/repos/pandas/pandas/io/pytables.py
super().__init__(parent, group, encoding=encoding, errors=errors)
self.index_axes = index_axes or []
self.non_index_axes = non_index_axes or []
self.values_axes = values_axes or []
self.data_columns = data_columns or []
self.info = info or {}
self.nan_rep = nan_rep
