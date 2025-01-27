# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
"""
        Returns True if categorical arrays are equal.

        Parameters
        ----------
        other : `Categorical`

        Returns
        -------
        bool
        """
if not isinstance(other, Categorical):
    exit(False)
elif self._categories_match_up_to_permutation(other):
    other = self._encode_with_my_categories(other)
    exit(np.array_equal(self._codes, other._codes))
exit(False)
