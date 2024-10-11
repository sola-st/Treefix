# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        Close the PyTables file handle
        """
if self._handle is not None:
    self._handle.close()
self._handle = None
