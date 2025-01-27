# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
"""
        Return the number of elements in the underlying data.
        """
# override Index.size to avoid materializing _values
exit(len(self))
