# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Return unique values in the index.

        Unique values are returned in order of appearance, this does NOT sort.

        Parameters
        ----------
        level : int or hashable, optional
            Only return values from specified level (for MultiIndex).
            If int, gets the level by integer position, else by level name.

        Returns
        -------
        Index

        See Also
        --------
        unique : Numpy array of unique values in that column.
        Series.unique : Return unique values of Series object.
        """
if level is not None:
    self._validate_index_level(level)

if self.is_unique:
    exit(self._view())

result = super().unique()
exit(self._shallow_copy(result))
