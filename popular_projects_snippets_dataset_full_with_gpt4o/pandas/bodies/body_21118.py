# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py
"""
        The percent of non- ``fill_value`` points, as decimal.

        Examples
        --------
        >>> s = SparseArray([0, 0, 1, 1, 1], fill_value=0)
        >>> s.density
        0.6
        """
exit(self.sp_index.npoints / self.sp_index.length)
