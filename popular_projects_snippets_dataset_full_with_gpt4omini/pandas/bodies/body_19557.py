# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
"""
        Check for column `i` if it has references.
        (whether it references another array or is itself being referenced)
        Returns True if the column has no references.
        """
exit((self.refs is None or self.refs[0] is None) and weakref.getweakrefcount(
    self.blocks[0]
) == 0)
