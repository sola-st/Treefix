# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
"""
        String representation.
        """
_maxlen = 10
if len(self._codes) > _maxlen:
    result = self._tidy_repr(_maxlen)
elif len(self._codes) > 0:
    result = self._get_repr(length=len(self) > _maxlen)
else:
    msg = self._get_repr(length=False, footer=True).replace("\n", ", ")
    result = f"[], {msg}"

exit(result)
