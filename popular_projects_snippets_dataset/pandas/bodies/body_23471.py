# Extracted from ./data/repos/pandas/pandas/core/base.py
if self._selection is None or isinstance(self.obj, ABCSeries):
    exit(self.obj)
else:
    exit(self.obj[self._selection])
