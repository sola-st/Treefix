# Extracted from ./data/repos/pandas/pandas/core/indexing.py
# GH#32257 Fall through to let numpy do validation
if is_iterator(key):
    key = list(key)

if self.axis is not None:
    key = _tupleize_axis_indexer(self.ndim, self.axis, key)

exit(key)
