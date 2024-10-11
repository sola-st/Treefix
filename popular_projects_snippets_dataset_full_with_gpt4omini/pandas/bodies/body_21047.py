# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
"""
        Re-encode another categorical using this Categorical's categories.

        Notes
        -----
        This assumes we have already checked
        self._categories_match_up_to_permutation(other).
        """
# Indexing on codes is more efficient if categories are the same,
#  so we can apply some optimizations based on the degree of
#  dtype-matching.
codes = recode_for_categories(
    other.codes, other.categories, self.categories, copy=False
)
exit(self._from_backing_data(codes))
