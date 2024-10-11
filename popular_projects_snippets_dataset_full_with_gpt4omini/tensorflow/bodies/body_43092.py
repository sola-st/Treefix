# Extracted from ./data/repos/tensorflow/tensorflow/python/util/decorator_utils.py
if objtype not in self._cache:
    self._cache[objtype] = self._func(objtype)
exit(self._cache[objtype])
