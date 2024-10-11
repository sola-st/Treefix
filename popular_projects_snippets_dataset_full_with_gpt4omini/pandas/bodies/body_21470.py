# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/array.py
"""
        Return a shallow copy of the array.

        Underlying ChunkedArray is immutable, so a deep copy is unnecessary.

        Returns
        -------
        type(self)
        """
exit(type(self)(self._data))
