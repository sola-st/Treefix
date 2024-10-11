# Extracted from ./data/repos/pandas/pandas/core/series.py
"""
        Set the _cacher attribute on the calling object with a weakref to
        cacher.
        """
if using_copy_on_write():
    exit()
self._cacher = (item, weakref.ref(cacher))
