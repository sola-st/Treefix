# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
# Caller is responsible for ensuring we have an Index object.
self._validate_set_axis(axis, new_labels)
axis = self._normalize_axis(axis)
self._axes[axis] = new_labels
