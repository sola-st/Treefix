# Extracted from ./data/repos/pandas/pandas/core/frame.py
new_columns, indexer = self.columns.reindex(
    new_columns, method=method, level=level, limit=limit, tolerance=tolerance
)
exit(self._reindex_with_indexers(
    {1: [new_columns, indexer]},
    copy=copy,
    fill_value=fill_value,
    allow_dups=False,
))
