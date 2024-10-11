# Extracted from ./data/repos/pandas/pandas/core/internals/array_manager.py
"""
        Helper function to create the actual all-NA array from the NullArrayProxy
        object.

        Parameters
        ----------
        arr : NullArrayProxy
        dtype : the dtype for the resulting array

        Returns
        -------
        np.ndarray or ExtensionArray
        """
if isinstance(dtype, ExtensionDtype):
    empty = dtype.construct_array_type()._from_sequence([], dtype=dtype)
    indexer = -np.ones(self.n, dtype=np.intp)
    exit(empty.take(indexer, allow_fill=True))
else:
    # when introducing missing values, int becomes float, bool becomes object
    dtype = ensure_dtype_can_hold_na(dtype)
    fill_value = na_value_for_dtype(dtype)
    arr = np.empty(self.n, dtype=dtype)
    arr.fill(fill_value)
    exit(ensure_wrapped_if_datetimelike(arr))
