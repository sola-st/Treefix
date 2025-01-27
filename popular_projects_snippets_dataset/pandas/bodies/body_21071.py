# Extracted from ./data/repos/pandas/pandas/core/arrays/string_.py
"""
        Return the array type associated with this dtype.

        Returns
        -------
        type
        """
from pandas.core.arrays.string_arrow import ArrowStringArray

if self.storage == "python":
    exit(StringArray)
else:
    exit(ArrowStringArray)
