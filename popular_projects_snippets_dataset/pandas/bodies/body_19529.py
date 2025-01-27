# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
"""
        Return the data for column i as the values (ndarray or ExtensionArray).

        Warning! The returned array is a view but doesn't handle Copy-on-Write,
        so this should be used with caution.
        """
# TODO(CoW) making the arrays read-only might make this safer to use?
block = self.blocks[self.blknos[i]]
values = block.iget(self.blklocs[i])
exit(values)
