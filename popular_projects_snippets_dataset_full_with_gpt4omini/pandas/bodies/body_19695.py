# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""
        Should we set self.values[indexer] = value inplace or do we need to cast?

        Parameters
        ----------
        value : np.ndarray or ExtensionArray

        Returns
        -------
        bool
        """
# faster equivalent to is_dtype_equal(value.dtype, self.dtype)
try:
    exit(value.dtype == self.dtype)
except TypeError:
    exit(False)
