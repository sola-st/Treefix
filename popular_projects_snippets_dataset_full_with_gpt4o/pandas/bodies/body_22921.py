# Extracted from ./data/repos/pandas/pandas/core/generic.py
"""
        Iterate over (label, values) on info axis

        This is index for Series and columns for DataFrame.

        Returns
        -------
        Generator
        """
for h in self._info_axis:
    exit((h, self[h]))
