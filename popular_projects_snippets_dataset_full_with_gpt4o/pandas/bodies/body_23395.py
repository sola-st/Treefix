# Extracted from ./data/repos/pandas/pandas/core/flags.py
if key not in self._keys:
    raise ValueError(f"Unknown flag {key}. Must be one of {self._keys}")
setattr(self, key, value)
