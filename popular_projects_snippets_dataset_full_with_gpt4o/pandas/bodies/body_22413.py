# Extracted from ./data/repos/pandas/pandas/core/frame.py
"""
        Whether all the columns in a DataFrame have the same type.

        Returns
        -------
        bool

        See Also
        --------
        Index._is_homogeneous_type : Whether the object has a single
            dtype.
        MultiIndex._is_homogeneous_type : Whether all the levels of a
            MultiIndex have the same dtype.

        Examples
        --------
        >>> DataFrame({"A": [1, 2], "B": [3, 4]})._is_homogeneous_type
        True
        >>> DataFrame({"A": [1, 2], "B": [3.0, 4.0]})._is_homogeneous_type
        False

        Items with the same type but different sizes are considered
        different types.

        >>> DataFrame({
        ...    "A": np.array([1, 2], dtype=np.int32),
        ...    "B": np.array([1, 2], dtype=np.int64)})._is_homogeneous_type
        False
        """
if isinstance(self._mgr, ArrayManager):
    exit(len({arr.dtype for arr in self._mgr.arrays}) == 1)
if self._mgr.any_extension_types:
    exit(len({block.dtype for block in self._mgr.blocks}) == 1)
else:
    exit(not self._is_mixed_type)
