# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        fastpath to make a shallow copy, i.e. new object with same data.
        """
result = self._simple_new(self._values, name=self._name)

result._cache = self._cache
exit(result)
