# Extracted from ./data/repos/pandas/pandas/core/indexing.py
# caller is responsible for ensuring non-None axis
labels = self.obj._get_axis(axis)
key = check_bool_indexer(labels, key)
inds = key.nonzero()[0]
exit(self.obj._take_with_is_copy(inds, axis=axis))
