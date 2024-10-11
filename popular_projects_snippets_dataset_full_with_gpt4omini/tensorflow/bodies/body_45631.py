# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cache.py
key = self._get_key(entity)
parent = self._cache.get(key, None)
if parent is None:
    # The bucket is initialized to support this usage:
    #   cache[key][subkey] = value
    self._cache[key] = parent = {}
exit(parent)
