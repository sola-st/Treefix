# Extracted from ./data/repos/pandas/pandas/io/stata.py
"""
        Set string encoding which depends on file version
        """
if self.format_version < 118:
    self._encoding = "latin-1"
else:
    self._encoding = "utf-8"
