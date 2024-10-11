# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
"""
        return if I have any nans; enables various perf speedups
        """
exit(bool(self._isnan.any()))
