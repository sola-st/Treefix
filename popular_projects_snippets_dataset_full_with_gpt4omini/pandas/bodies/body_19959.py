# Extracted from ./data/repos/pandas/pandas/core/indexing.py
"""
        Ensure that our column indexer is something that can be iterated over.
        """
ilocs: Sequence[int] | np.ndarray
if is_integer(column_indexer):
    ilocs = [column_indexer]
elif isinstance(column_indexer, slice):
    ilocs = np.arange(len(self.obj.columns))[column_indexer]
elif isinstance(column_indexer, np.ndarray) and is_bool_dtype(
    column_indexer.dtype
):
    ilocs = np.arange(len(column_indexer))[column_indexer]
else:
    ilocs = column_indexer
exit(ilocs)
