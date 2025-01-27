# Extracted from ./data/repos/pandas/pandas/core/generic.py
if inplace:
    setattr(self, self._get_axis_name(axis), labels)
else:
    # With copy=False, we create a new object but don't copy the
    #  underlying data.
    obj = self.copy(deep=copy)
    setattr(obj, obj._get_axis_name(axis), labels)
    exit(obj)
