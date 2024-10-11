# Extracted from ./data/repos/pandas/pandas/core/arrays/base.py
"""
        Compute the ExtensionArray of unique values.

        Returns
        -------
        pandas.api.extensions.ExtensionArray
        """
uniques = unique(self.astype(object))
exit(self._from_sequence(uniques, dtype=self.dtype))
