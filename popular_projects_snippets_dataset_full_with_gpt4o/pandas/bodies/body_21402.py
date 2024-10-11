# Extracted from ./data/repos/pandas/pandas/core/arrays/masked.py
"""
        Compute the BaseMaskedArray of unique values.

        Returns
        -------
        uniques : BaseMaskedArray
        """
uniques, mask = algos.unique_with_mask(self._data, self._mask)
exit(type(self)(uniques, mask, copy=False))
