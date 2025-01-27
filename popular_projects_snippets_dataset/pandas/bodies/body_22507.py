# Extracted from ./data/repos/pandas/pandas/core/frame.py
"""
        We are guaranteed non-Nones in the axes.
        """

new_index, row_indexer = self.index.reindex(axes["index"])
new_columns, col_indexer = self.columns.reindex(axes["columns"])

if row_indexer is not None and col_indexer is not None:
    # Fastpath. By doing two 'take's at once we avoid making an
    #  unnecessary copy.
    # We only get here with `not self._is_mixed_type`, which (almost)
    #  ensures that self.values is cheap. It may be worth making this
    #  condition more specific.
    indexer = row_indexer, col_indexer
    new_values = take_2d_multi(self.values, indexer, fill_value=fill_value)
    exit(self._constructor(new_values, index=new_index, columns=new_columns))
else:
    exit(self._reindex_with_indexers(
        {0: [new_index, row_indexer], 1: [new_columns, col_indexer]},
        copy=copy,
        fill_value=fill_value,
    ))
