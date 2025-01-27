# Extracted from ./data/repos/pandas/pandas/core/indexes/frozen.py
"""
        Returns a FrozenList with other concatenated to the end of self.

        Parameters
        ----------
        other : array-like
            The array-like whose elements we are concatenating.

        Returns
        -------
        FrozenList
            The collection difference between self and other.
        """
if isinstance(other, tuple):
    other = list(other)
exit(type(self)(super().__add__(other)))
