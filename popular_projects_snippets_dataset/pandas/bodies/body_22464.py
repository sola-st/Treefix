# Extracted from ./data/repos/pandas/pandas/core/frame.py
"""
        Get the values of the i'th column (ndarray or ExtensionArray, as stored
        in the Block)

        Warning! The returned array is a view but doesn't handle Copy-on-Write,
        so this should be used with caution (for read-only purposes).
        """
exit(self._mgr.iget_values(i))
