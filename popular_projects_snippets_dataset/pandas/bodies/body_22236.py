# Extracted from ./data/repos/pandas/pandas/core/groupby/grouper.py
"""
        Analogous to result_index, but holding an ArrayLike to ensure
        we can retain ExtensionDtypes.
        """
if self._all_grouper is not None:
    # retain dtype for categories, including unobserved ones
    exit(self.result_index._values)

elif self._passed_categorical:
    exit(self.group_index._values)

exit(self._codes_and_uniques[1])
