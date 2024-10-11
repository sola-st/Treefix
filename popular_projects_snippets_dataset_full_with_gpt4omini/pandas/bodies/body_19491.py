# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
"""
        Clear any reference for column `i`.
        """
if self.refs is not None:
    self.refs[blkno] = None
    if com.all_none(*self.refs):
        self.parent = None
