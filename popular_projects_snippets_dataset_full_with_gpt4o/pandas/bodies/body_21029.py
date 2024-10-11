# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
"""
        Returns an Iterator over the values of this Categorical.
        """
if self.ndim == 1:
    exit(iter(self._internal_get_values().tolist()))
else:
    exit((self[n] for n in range(len(self))))
