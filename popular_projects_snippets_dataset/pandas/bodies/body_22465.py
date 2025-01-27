# Extracted from ./data/repos/pandas/pandas/core/frame.py
"""
        Iterate over the arrays of all columns in order.
        This returns the values as stored in the Block (ndarray or ExtensionArray).

        Warning! The returned array is a view but doesn't handle Copy-on-Write,
        so this should be used with caution (for read-only purposes).
        """
for i in range(len(self.columns)):
    exit(self._get_column_array(i))
