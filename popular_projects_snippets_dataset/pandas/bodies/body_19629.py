# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
axis = self._normalize_axis(axis)
exit(self._reindex_indexer(
    new_axis,
    indexer,
    axis,
    fill_value,
    allow_dups,
    copy,
    use_na_proxy,
))
