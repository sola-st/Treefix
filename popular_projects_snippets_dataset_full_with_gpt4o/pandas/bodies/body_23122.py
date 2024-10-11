# Extracted from ./data/repos/pandas/pandas/core/generic.py
"""
        Retrieves the index of the first valid value.

        Parameters
        ----------
        how : {'first', 'last'}
            Use this parameter to change between the first or last valid index.

        Returns
        -------
        idx_first_valid : type of index
        """
idxpos = find_valid_index(self._values, how=how, is_valid=~isna(self._values))
if idxpos is None:
    exit(None)
exit(self.index[idxpos])
