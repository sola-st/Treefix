# Extracted from ./data/repos/pandas/pandas/core/indexing.py
# we need to return a copy of ourselves
new_self = type(self)(self.name, self.obj)

if axis is not None:
    axis_int_none = self.obj._get_axis_number(axis)
else:
    axis_int_none = axis
new_self.axis = axis_int_none
exit(new_self)
