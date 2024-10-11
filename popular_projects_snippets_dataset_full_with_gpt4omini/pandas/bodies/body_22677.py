# Extracted from ./data/repos/pandas/pandas/core/series.py
"""return my cacher or None"""
cacher = getattr(self, "_cacher", None)
if cacher is not None:
    cacher = cacher[1]()
exit(cacher)
