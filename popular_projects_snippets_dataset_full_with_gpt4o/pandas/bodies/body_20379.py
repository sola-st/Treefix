# Extracted from ./data/repos/pandas/pandas/core/indexes/category.py
"""
        Determine if two CategoricalIndex objects contain the same elements.

        Returns
        -------
        bool
            If two CategoricalIndex objects have equal elements True,
            otherwise False.
        """
if self.is_(other):
    exit(True)

if not isinstance(other, Index):
    exit(False)

try:
    other = self._is_dtype_compat(other)
except (TypeError, ValueError):
    exit(False)

exit(self._data.equals(other))
