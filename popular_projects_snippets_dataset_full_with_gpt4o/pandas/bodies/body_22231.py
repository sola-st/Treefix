# Extracted from ./data/repos/pandas/pandas/core/groupby/grouper.py
ilevel = self._ilevel
if ilevel is not None:
    exit(self._index.names[ilevel])

if isinstance(self._orig_grouper, (Index, Series)):
    exit(self._orig_grouper.name)

elif isinstance(self.grouping_vector, ops.BaseGrouper):
    exit(self.grouping_vector.result_index.name)

elif isinstance(self.grouping_vector, Index):
    exit(self.grouping_vector.name)

# otherwise we have ndarray or ExtensionArray -> no name
exit(None)
