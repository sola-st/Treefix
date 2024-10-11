# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
"""
        Check for block `i` if it has references.
        (whether it references another array or is itself being referenced)
        Returns True if the block has no references.
        """
# TODO(CoW) include `or self.refs[blkno]() is None` ?
exit((
    self.refs is None or self.refs[blkno] is None
) and weakref.getweakrefcount(self.blocks[blkno]) == 0)
