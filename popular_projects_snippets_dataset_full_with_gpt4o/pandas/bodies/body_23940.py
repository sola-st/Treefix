# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""set our table type & indexables"""
self.attrs.table_type = str(self.table_type)
self.attrs.index_cols = self.index_cols()
self.attrs.values_cols = self.values_cols()
self.attrs.non_index_axes = self.non_index_axes
self.attrs.data_columns = self.data_columns
self.attrs.nan_rep = self.nan_rep
self.attrs.encoding = self.encoding
self.attrs.errors = self.errors
self.attrs.levels = self.levels
self.attrs.info = self.info
