# Extracted from ./data/repos/pandas/pandas/core/indexing.py
"""
        This is pretty simple as we just have to deal with labels.
        """
# caller is responsible for ensuring non-None axis
obj = self.obj
if not need_slice(slice_obj):
    exit(obj.copy(deep=False))

labels = obj._get_axis(axis)
indexer = labels.slice_indexer(slice_obj.start, slice_obj.stop, slice_obj.step)

if isinstance(indexer, slice):
    exit(self.obj._slice(indexer, axis=axis))
else:
    # DatetimeIndex overrides Index.slice_indexer and may
    #  return a DatetimeIndex instead of a slice object.
    exit(self.obj.take(indexer, axis=axis))
