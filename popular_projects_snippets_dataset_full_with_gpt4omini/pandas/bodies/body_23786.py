# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        return a boolean indicating whether the file is open
        """
if self._handle is None:
    exit(False)
exit(bool(self._handle.isopen))
