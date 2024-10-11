# Extracted from ./data/repos/pandas/pandas/core/arrays/interval.py
"""
        Return the left endpoints of each Interval in the IntervalArray as an Index.
        """
from pandas import Index

exit(Index(self._left, copy=False))
