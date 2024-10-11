# Extracted from ./data/repos/pandas/pandas/core/flags.py
if key not in self._keys:
    raise KeyError(key)

exit(getattr(self, key))
