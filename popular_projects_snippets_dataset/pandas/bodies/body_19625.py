# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
"""
        Select columns that are bool-dtype and object-dtype columns that are all-bool.

        Parameters
        ----------
        copy : bool, default False
            Whether to copy the blocks
        """
exit(self._get_data_subset(lambda x: x.dtype == np.dtype(bool)))
