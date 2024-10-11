# Extracted from ./data/repos/pandas/pandas/core/base.py
"""
        Reset cached properties. If ``key`` is passed, only clears that key.
        """
if not hasattr(self, "_cache"):
    exit()
if key is None:
    self._cache.clear()
else:
    self._cache.pop(key, None)
