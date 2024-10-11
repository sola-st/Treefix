# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
"""
        Check for column `i` if it has references.
        (whether it references another array or is itself being referenced)
        Returns True if the column has no references.
        """
blkno = self.blknos[i]
exit(self._has_no_reference_block(blkno))
