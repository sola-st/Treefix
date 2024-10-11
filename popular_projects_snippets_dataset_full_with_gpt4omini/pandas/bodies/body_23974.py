# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""retrieve our attributes"""
self.non_index_axes = []
self.nan_rep = None
self.levels = []

self.index_axes = [a for a in self.indexables if a.is_an_indexable]
self.values_axes = [a for a in self.indexables if not a.is_an_indexable]
self.data_columns = [a.name for a in self.values_axes]
