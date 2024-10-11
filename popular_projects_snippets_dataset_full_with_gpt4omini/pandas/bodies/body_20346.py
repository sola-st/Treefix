# Extracted from ./data/repos/pandas/pandas/core/indexes/range.py
result = type(self)._simple_new(self._range, name=self._name)
result._cache = self._cache
exit(result)
