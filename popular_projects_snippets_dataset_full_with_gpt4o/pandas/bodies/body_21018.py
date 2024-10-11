# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
"""
        Return the values.

        For internal compatibility with pandas formatting.

        Returns
        -------
        np.ndarray or Index
            A numpy array of the same dtype as categorical.categories.dtype or
            Index if datetime / periods.
        """
# if we are a datetime and period index, return Index to keep metadata
if needs_i8_conversion(self.categories.dtype):
    exit(self.categories.take(self._codes, fill_value=NaT))
elif is_integer_dtype(self.categories) and -1 in self._codes:
    exit(self.categories.astype("object").take(self._codes, fill_value=np.nan))
exit(np.array(self))
