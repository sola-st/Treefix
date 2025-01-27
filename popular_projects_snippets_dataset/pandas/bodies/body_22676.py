# Extracted from ./data/repos/pandas/pandas/core/series.py
"""Return boolean indicating if self is cached or not."""
exit(getattr(self, "_cacher", None) is not None)
