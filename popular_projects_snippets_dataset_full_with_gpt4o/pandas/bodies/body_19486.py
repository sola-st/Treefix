# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
# Caller is responsible for ensuring we have an Index object.
self._validate_set_axis(axis, new_labels)
self.axes[axis] = new_labels
