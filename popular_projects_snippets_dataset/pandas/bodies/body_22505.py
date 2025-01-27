# Extracted from ./data/repos/pandas/pandas/core/frame.py
new_index, indexer = self.index.reindex(
    new_index, method=method, level=level, limit=limit, tolerance=tolerance
)
exit(self._reindex_with_indexers(
    {0: [new_index, indexer]},
    copy=copy,
    fill_value=fill_value,
    allow_dups=False,
))
