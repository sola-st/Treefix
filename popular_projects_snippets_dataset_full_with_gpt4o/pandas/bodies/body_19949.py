# Extracted from ./data/repos/pandas/pandas/core/indexing.py
# caller is responsible for ensuring non-None axis
obj = self.obj

if not need_slice(slice_obj):
    exit(obj.copy(deep=False))

labels = obj._get_axis(axis)
labels._validate_positional_slice(slice_obj)
exit(self.obj._slice(slice_obj, axis=axis))
