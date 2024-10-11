# Extracted from ./data/repos/pandas/pandas/core/indexes/interval.py
"""
        Return True if the IntervalIndex is monotonic decreasing (only equal or
        decreasing values), else False
        """
exit(self[::-1].is_monotonic_increasing)
