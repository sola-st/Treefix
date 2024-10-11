# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
"""
        Return a boolean if the values are equal or decreasing.
        """
# monotonic decreasing if and only if reverse is monotonic increasing
exit(self[::-1].is_monotonic_increasing)
