# Extracted from ./data/repos/pandas/pandas/core/strings/base.py
if isinstance(key, slice):
    exit(self._str_slice(start=key.start, stop=key.stop, step=key.step))
else:
    exit(self._str_get(key))
