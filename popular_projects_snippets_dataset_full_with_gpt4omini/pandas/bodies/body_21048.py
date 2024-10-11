# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
"""
        Returns True if categoricals are the same dtype
          same categories, and same ordered

        Parameters
        ----------
        other : Categorical

        Returns
        -------
        bool
        """
exit(hash(self.dtype) == hash(other.dtype))
