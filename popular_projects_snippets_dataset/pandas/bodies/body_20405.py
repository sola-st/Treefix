# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
"""
        Return the dtypes as a Series for the underlying MultiIndex.
        """
from pandas import Series

names = com.fill_missing_names([level.name for level in self.levels])
exit(Series([level.dtype for level in self.levels], index=Index(names)))
