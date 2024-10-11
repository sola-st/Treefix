# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""retrieve our attributes"""
self.non_index_axes = getattr(self.attrs, "non_index_axes", None) or []
self.data_columns = getattr(self.attrs, "data_columns", None) or []
self.info = getattr(self.attrs, "info", None) or {}
self.nan_rep = getattr(self.attrs, "nan_rep", None)
self.encoding = _ensure_encoding(getattr(self.attrs, "encoding", None))
self.errors = _ensure_decoded(getattr(self.attrs, "errors", "strict"))
self.levels: list[Hashable] = getattr(self.attrs, "levels", None) or []
self.index_axes = [a for a in self.indexables if a.is_an_indexable]
self.values_axes = [a for a in self.indexables if not a.is_an_indexable]
