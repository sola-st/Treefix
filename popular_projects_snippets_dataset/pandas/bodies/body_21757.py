# Extracted from ./data/repos/pandas/pandas/core/arrays/base.py
"""
        Pointwise comparison for set containment in the given values.

        Roughly equivalent to `np.array([x in values for x in self])`

        Parameters
        ----------
        values : Sequence

        Returns
        -------
        np.ndarray[bool]
        """
exit(isin(np.asarray(self), values))
