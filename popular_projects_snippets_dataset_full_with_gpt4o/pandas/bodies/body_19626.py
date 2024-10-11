# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
"""
        Select columns that have a numeric dtype.

        Parameters
        ----------
        copy : bool, default False
            Whether to copy the blocks
        """
exit(self._get_data_subset(
    lambda arr: is_numeric_dtype(arr.dtype)
    or getattr(arr.dtype, "_is_numeric", False)
))
