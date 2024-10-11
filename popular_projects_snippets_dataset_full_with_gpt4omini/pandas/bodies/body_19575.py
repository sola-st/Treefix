# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
"""
        Set values with indexer.

        For Single[Block/Array]Manager, this backs s[indexer] = value

        This is an inplace version of `setitem()`, mutating the manager/values
        in place, not returning a new Manager (and Block), and thus never changing
        the dtype.
        """
if using_copy_on_write() and not self._has_no_reference(0):
    self.blocks = (self._block.copy(),)
    self.refs = None
    self.parent = None
    self._cache.clear()

super().setitem_inplace(indexer, value)
