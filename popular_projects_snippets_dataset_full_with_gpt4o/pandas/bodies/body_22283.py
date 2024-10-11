# Extracted from ./data/repos/pandas/pandas/core/resample.py
if attr in self._internal_names_set:
    exit(object.__getattribute__(self, attr))
if attr in self._attributes:
    exit(getattr(self.groupby, attr))
if attr in self.obj:
    exit(self[attr])

exit(object.__getattribute__(self, attr))
