# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py
"""
        Convert SparseArray to a NumPy array.

        Returns
        -------
        arr : NumPy array
        """
exit(np.asarray(self, dtype=self.sp_values.dtype))
