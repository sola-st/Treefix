# Extracted from ./data/repos/pandas/pandas/io/stata.py
"""
        Helper to call encode before writing to file for Python 3 compat.
        """
self.handles.handle.write(to_write.encode(self._encoding))
