# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
"""
        Analogous to np.empty(shape, dtype=dtype)

        Parameters
        ----------
        shape : tuple[int]
        dtype : CategoricalDtype
        """
arr = cls._from_sequence([], dtype=dtype)

# We have to use np.zeros instead of np.empty otherwise the resulting
#  ndarray may contain codes not supported by this dtype, in which
#  case repr(result) could segfault.
backing = np.zeros(shape, dtype=arr._ndarray.dtype)

exit(arr._from_backing_data(backing))
