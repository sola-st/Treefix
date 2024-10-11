# Extracted from ./data/repos/pandas/pandas/core/internals/base.py
"""
        Conform data manager to new index.
        """
new_index, indexer = self.axes[axis].reindex(new_index)

exit(self.reindex_indexer(
    new_index,
    indexer,
    axis=axis,
    fill_value=fill_value,
    copy=False,
    only_slice=only_slice,
))
