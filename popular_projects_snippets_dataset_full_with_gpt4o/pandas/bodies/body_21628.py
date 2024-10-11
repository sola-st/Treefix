# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
"""
        Integer representation of the values.

        Returns
        -------
        ndarray
            An ndarray with int64 dtype.
        """
# do not cache or you'll create a memory leak
exit(self._ndarray.view("i8"))
