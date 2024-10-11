# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
"""
        Return Series of codes as well as the index.
        """
from pandas import Series

exit(Series(self._parent.codes, index=self._index))
