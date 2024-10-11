# Extracted from ./data/repos/pandas/pandas/core/generic.py
"""
        Return a tuple of axis dimensions
        """
exit(tuple(len(self._get_axis(a)) for a in self._AXIS_ORDERS))
