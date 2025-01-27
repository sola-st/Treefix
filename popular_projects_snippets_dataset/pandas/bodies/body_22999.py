# Extracted from ./data/repos/pandas/pandas/core/generic.py
"""
        Compute NDFrame with "consolidated" internals (data of each dtype
        grouped together in a single ndarray).

        Returns
        -------
        consolidated : same type as caller
        """
f = lambda: self._mgr.consolidate()
cons_data = self._protect_consolidate(f)
exit(self._constructor(cons_data).__finalize__(self))
