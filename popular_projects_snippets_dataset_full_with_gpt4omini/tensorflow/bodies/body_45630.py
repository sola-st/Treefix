# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cache.py
key = self._get_key(entity)
parent = self._cache.get(key, None)
if parent is None:
    exit(False)
exit(subkey in parent)
