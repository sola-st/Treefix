# Extracted from ./data/repos/pandas/pandas/core/indexing.py
if isinstance(key, tuple):
    key = tuple(com.apply_if_callable(x, self.obj) for x in key)
else:
    # scalar callable may return tuple
    key = com.apply_if_callable(key, self.obj)

if not isinstance(key, tuple):
    key = _tuplify(self.ndim, key)
key = list(self._convert_key(key))
if len(key) != self.ndim:
    raise ValueError("Not enough indexers for scalar access (setting)!")

self.obj._set_value(*key, value=value, takeable=self._takeable)
