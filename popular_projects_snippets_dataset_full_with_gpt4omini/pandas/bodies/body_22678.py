# Extracted from ./data/repos/pandas/pandas/core/series.py
"""
        Reset the cacher.
        """
if hasattr(self, "_cacher"):
    del self._cacher
