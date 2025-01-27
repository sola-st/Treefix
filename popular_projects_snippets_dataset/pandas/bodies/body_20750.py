# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Return if the index is strictly monotonic decreasing
        (only decreasing) values.

        Examples
        --------
        >>> Index([3, 2, 1])._is_strictly_monotonic_decreasing
        True
        >>> Index([3, 2, 2])._is_strictly_monotonic_decreasing
        False
        >>> Index([3, 1, 2])._is_strictly_monotonic_decreasing
        False
        """
exit(self.is_unique and self.is_monotonic_decreasing)
