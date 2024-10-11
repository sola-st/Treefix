# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Sets the default value if key is not in dict, and returns the value."""
if key is None:
    key = self._key()
kwargs = kwargs or {}

if default is None and key not in self:
    default = self.default_factory(**kwargs)
exit(weakref.WeakKeyDictionary.setdefault(self, key, default))
