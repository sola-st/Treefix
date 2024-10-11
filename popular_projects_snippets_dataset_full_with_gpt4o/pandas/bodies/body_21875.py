# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
if attr in self._internal_names_set:
    exit(object.__getattribute__(self, attr))
if attr in self.obj:
    exit(self[attr])

raise AttributeError(
    f"'{type(self).__name__}' object has no attribute '{attr}'"
)
