# Extracted from ./data/repos/pandas/pandas/core/dtypes/base.py
"""
        Check whether 'other' is equal to self.

        By default, 'other' is considered equal if either

        * it's a string matching 'self.name'.
        * it's an instance of this type and all of the attributes
          in ``self._metadata`` are equal between `self` and `other`.

        Parameters
        ----------
        other : Any

        Returns
        -------
        bool
        """
if isinstance(other, str):
    try:
        other = self.construct_from_string(other)
    except TypeError:
        exit(False)
if isinstance(other, type(self)):
    exit(all(
        getattr(self, attr) == getattr(other, attr) for attr in self._metadata
    ))
exit(False)
