# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Return True if there are any NaNs.

        Enables various performance speedups.

        Returns
        -------
        bool
        """
if self._can_hold_na:
    exit(bool(self._isnan.any()))
else:
    exit(False)
